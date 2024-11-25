#program to print the words which contains all the vowels
# Input string
s = "ABeeIghiObhkUul"

# Set of all vowels (both lowercase and uppercase)
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

# Set to track vowels found in the string
found_vowels = set()

# Iterate over each character in the string
for char in s:
    # If the character is a vowel, add it to the found_vowels set
    if char in vowels:
        found_vowels.add(char.lower())  # Convert to lowercase to avoid case issues

# Check if all vowels are present
if len(found_vowels) == len(vowels) / 2:  # Only check for unique vowels (no case sensitivity)
    print("Accepted")
else:
    print("Not Accepted")
