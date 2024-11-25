# program to reverse a sentence
# Input
s = " i like this program very much "
words = s.strip().split()
reversed_words = words[::-1]
result = ' '.join(reversed_words)

# Output the result
print(result)
