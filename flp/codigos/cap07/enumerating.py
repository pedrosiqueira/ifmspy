class CustomSequence:
    def __len__(self):
        return 5

    def __getitem__(self, index):
        return f"x{index}"


class FunkyBackwards:
    pass

normal_list = [1, 2, 3, 4, 5]
custom = CustomSequence()
funky = FunkyBackwards()

for item in reversed(normal_list):
    print(item, end=", ")
print()

for item in reversed(custom):
    print(item, end=", ")
print()

for item in reversed(funky):
    print(item, end=", ")
print()
