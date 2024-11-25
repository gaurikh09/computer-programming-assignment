#program to capitalize frist and last letter of a string
# Input string
s = "welcome you "
words = s.split()

# Initialize a result list to store transformed words
result = []
for word in words:
    if len(word) > 1:
        # Capitalize the first and last characters
        new_word = word[0].upper() + word[1:-1] + word[-1].upper()
    else:
        # If the word is a single character, capitalize it
        new_word = word.upper()
    result.append(new_word)

# Join the transformed words back into a single string
final_result = " ".join(result)

# Print the result
print(final_result)
