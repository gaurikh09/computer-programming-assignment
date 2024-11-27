# most freuent element in a list using dicitionary
# Define the list of elements
elements = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Initialize a dictionary to store the frequency of each element
frequency_dict = {}

# Count the frequency of each element
for item in elements:
    if item in frequency_dict:
        frequency_dict[item] += 1
    else:
        frequency_dict[item] = 1

# Find the element with the highest frequency
max_freq = 0
max_element = None
for item in elements:
    if frequency_dict[item] > max_freq:
        max_freq = frequency_dict[item]
        max_element = item

# Output the result
print(max_element)  # Output: "apple"
