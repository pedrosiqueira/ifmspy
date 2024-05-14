import re
import sys
import json
from pathlib import Path

DIRECTIVE_RE = re.compile(r"/\*\*\s*" r"(include|variable|loopover|endloop|loopvar)" r"\s*([^ *]*)" r"\s*\*\*/")


class TemplateEngine:
    def __init__(self, infilename, outfilename, contextfilename):
        self.template = open(infilename).read()
        self.working_dir = Path(infilename).absolute().parent
        self.pos = 0
        self.outfile = open(outfilename, "w")
        with open(contextfilename) as contextfile:
            self.context = json.load(contextfile)

    def process(self):
        match = DIRECTIVE_RE.search(self.template, pos=self.pos)
        while match:
            self.outfile.write(self.template[self.pos : match.start()])
            directive, argument = match.groups()
            method_name = "process_{}".format(directive)
            getattr(self, method_name)(match, argument)
            match = DIRECTIVE_RE.search(self.template, pos=self.pos)
        self.outfile.write(self.template[self.pos :])
        self.outfile.close()

    def process_include(self, match, argument):
        with (self.working_dir / argument).open() as includefile:
            self.outfile.write(includefile.read())
            self.pos = match.end()

    def process_variable(self, match, argument):
        self.outfile.write(self.context.get(argument, ""))
        self.pos = match.end()

    def process_loopover(self, match, argument):
        self.loop_index = 0
        self.loop_list = self.context.get(argument, [])
        self.pos = self.loop_beginning = match.end()

    def process_loopvar(self, match, argument):
        self.outfile.write(self.loop_list[self.loop_index])
        self.pos = match.end()

    def process_endloop(self, match, argument):
        self.loop_index += 1
        if self.loop_index < len(self.loop_list):
            self.pos = self.loop_beginning
        else:
            self.pos = match.end()


if __name__ == "__main__":
    infilename, outfilename, contextfilename = sys.argv[1:]
    engine = TemplateEngine(infilename, outfilename, contextfilename)
    engine.process()
