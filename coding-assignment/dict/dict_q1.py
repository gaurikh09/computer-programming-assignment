#program to merge two dicitionaries
# Define the dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "d": 5}

# Merge the dictionaries
dict1.update(dict2)

# Output the merged dictionary
print(dict1)  # Output: {"a": 1, "b": 4, "c": 3, "d": 5}
