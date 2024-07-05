import time
from datetime import datetime


def call_after(delay, callback, **kwargs):
    time.sleep(delay)
    callback(**kwargs)


def format_time(message):
    print(datetime.now(), message)


class Repeater:
    def __init__(self, times=3, delay=1):
        self.count = 0
        self.times = times
        self.delay = delay

    def repeat(self):
        format_time(f"repeat {self.count}")
        self.count += 1
        if self.count < self.times:
            call_after(self.delay, self.repeat)


format_time("Valendo!")
repeater = Repeater()
call_after(4, repeater.repeat)
