# find words that are freater then the given length
# Input string and length k
string = "hello this is computer science portal"
k = int(input())

# Split the string into words
words = string.split()
result = [word for word in words if len(word) > k]

# Output the result
print("Words longer than", k, ":", " ".join(result))
