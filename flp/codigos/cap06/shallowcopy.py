from dataclasses import make_dataclass
from copy import copy, deepcopy

Point = make_dataclass("Point", ("x", "y"))

original = [Point(0, 0), Point(1, 1)]
reference = original
shallowcopied1 = original.copy()
shallowcopied2 = copy(original)
deepcopied = deepcopy(original)

original.append(Point(2, 4))
original[0].x, original[0].y = 3, 9

shallowcopied1.append(Point(4, 16))

shallowcopied2[1].x, original[1].y = 5, 25

print("Original Points:      ", original)
print("Reference Points:     ", reference)
print("Shallow Copied Points:", shallowcopied1)
print("Also Shallow Copy:    ", shallowcopied2)
print("Deep Copied Points:   ", deepcopied)