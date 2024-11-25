# program to convert uppercase string to lowercase
# Input string
s = "ABCddE"

# Initialize an empty result string
result = ""

# Iterate over each character in the string
for char in s:
    # If the character is uppercase, convert it to lowercase
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)  # Convert uppercase to lowercase
    else:
        result += char  

# Output
print(result)
#output-abcdde
