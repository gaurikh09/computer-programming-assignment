# program to count number of vowels
# Input string
s = "abcdefghijk"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

#counter for vowels
count = 0

# Traverse each character in the string
for char in s:
    if char in vowels:  # Check 
        count += 1

# total number of vowels
print("No. of vowels:", count)
