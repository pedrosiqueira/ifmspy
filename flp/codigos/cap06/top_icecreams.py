from collections import Counter

responses = [
    "vanilla",
    "chocolate",
    "vanilla",
    "vanilla",
    "caramel",
    "chocolate",
    "strawberry",
    "vanilla",
]

print("The children voted for", Counter(responses).most_common(1)[0][0], "ice cream")