# program to give sum of numbers present in a string
# Input string
s = "1abc23
current_num = 0
total_sum = 0
for char in s:
    if char.isdigit():  # Check if the character is a digit
        current_num = current_num * 10 + int(char)  
    else:
        total_sum += current_num 
        current_num = 0  # Reset the number

# Add the last number if it exists
total_sum += current_num

# Output the result
print(total_sum)

