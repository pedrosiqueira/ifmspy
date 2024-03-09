class WeirdSortee:
    def __init__(self, string, number):
        self.string = string
        self.number = number

    def __lt__(self, other):
        return self.number < other.number

    def __repr__(self):
        return f"{self.string}:{self.number}"


a = WeirdSortee("a", 4)
b = WeirdSortee("B", 3)
c = WeirdSortee("c", 2)
d = WeirdSortee("d", 1)
l = [a, b, c, d]
print(l)
l.sort()
print(l)


def custom_order(obj):
    return obj.string.lower()

l.sort(key=custom_order)
print(l)
