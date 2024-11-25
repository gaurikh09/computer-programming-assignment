# program to replace dot and comma
# Input string
s = "14,625,498.002"
result = ""
for char in s:
    if char == ',':  # Replace comma with dot
        result += '.'
    elif char == '.':  # Replace dot with comma
        result += ','
    else:  # Leave other characters unchanged
        result += char

# Print the transformed string
print(result)
