# program to  print longest name from a given strig
# Input
names = ["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks"]

# The longest name as the first name in the list
longest_name = names[0]

# Iterate through the list of names starting from the second element
for name in names:
    if len(name) > len(longest_name):
        longest_name = name

# Output the longest name
print(longest_name)
