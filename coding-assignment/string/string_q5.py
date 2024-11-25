# remove duplicate elements from strings
# Input string
string = "geEksforGEeks"

# Initialize a set to track seen characters and a list for the result
s = set()
result = []

# Iterate over the characters in the string
for char in string:
    if char not in s:
        s.add(char)  # Mark the character as seen
        result.append(char)  # Add it to the result list

# Convert the result list to a string and print
output = ''.join(result)
print(output)

#output-geEksforG

