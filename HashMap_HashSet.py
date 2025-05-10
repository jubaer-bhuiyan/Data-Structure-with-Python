# HashMap Example (Dictionary)
my_map = {
    "apple": 5,
    "banana": 3,
    "orange": 7
}

# Access
print("Apple count:", my_map["apple"])

# Update
my_map["banana"] = 4

# Insert
my_map["grape"] = 10

# Delete
del my_map["orange"]

# Check key existence
print("banana" in my_map)  # True

print("\nHashMap (dict) Content:")
for key, value in my_map.items():
    print(f"{key}: {value}")

print("\n---------------------\n")

# HashSet Example (Set)
my_set = set(["apple", "banana", "orange", "banana"])

# Add
my_set.add("grape")

# Remove
my_set.discard("orange")

# Check membership
print("apple" in my_set)  # True

print("\nHashSet (set) Content:")
for item in my_set:
    print(item)
