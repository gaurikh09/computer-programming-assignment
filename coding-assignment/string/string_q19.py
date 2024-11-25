# program to print even length strings
# Input string
s = "This is a python language"

# Split the string into words
words = s.split()

# Iterate over each word
for word in words:
    # Check if the length of the word is even
    if len(word) % 2 == 0:
        # Print the word if its length is even
        print(word, end=" ")
