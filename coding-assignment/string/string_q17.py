# program to see that it has atleast one alphabet and one number
# Input string
str = "welcome2ourcountry34"
has_letter = False
has_number = False
for char in str:
    if char.isalpha():  # Check if the character is a letter
        has_letter = True
    if char.isdigit():  # Check if the character is a number
        has_number = True
    if has_letter and has_number:
        break

# Output result
print(has_letter and has_number)
