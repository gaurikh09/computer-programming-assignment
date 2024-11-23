#program to reverse the sentence
# Input string
s = " i like this program very much "

#  Remove leading, trailing, and extra spaces
words = s.split()  # Splits the string into a list of words, removing extra spaces

#  Reverse the list of words
reversed_words = words[::-1]  # Reverses the list of words

#  Join the reversed words with a single space
result = ' '.join(reversed_words)  # Joins the words with a single space

# Output the result
print(result)
