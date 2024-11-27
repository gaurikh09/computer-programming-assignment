# 1. Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# 2. Accessing elements of a tuple
first_element = my_tuple[0]  # Accessing the first element
last_element = my_tuple[-1]  # Accessing the last element

# 3. Concatenating tuples
another_tuple = (6, 7, 8)
combined_tuple = my_tuple + another_tuple  # Concatenating tuples

# 4. Slicing a tuple
sliced_tuple = my_tuple[1:4]  # Getting elements from index 1 to 3 (inclusive of 1, exclusive of 4)

# 5. Finding the length of a tuple
tuple_length = len(my_tuple)

# Output the results
print("First Element:", first_element)  # Output: 1
print("Last Element:", last_element)    # Output: 5
print("Combined Tuple:", combined_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)
print("Sliced Tuple:", sliced_tuple)  # Output: (2, 3, 4)
print("Length of Tuple:", tuple_length)  # Output: 5
