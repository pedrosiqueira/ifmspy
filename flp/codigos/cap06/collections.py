my_collection = {
    "Sarah Brightman",
    "Guns N' Roses",
    "Opeth",
    "Vixy and Tony",
}

your_collection = {"Nickelback", "Guns N' Roses", "Savage Garden"}

print("All:", my_collection.union(your_collection))
print("Both:", your_collection.intersection(my_collection))
print("Either but not both:", my_collection.symmetric_difference(your_collection))
