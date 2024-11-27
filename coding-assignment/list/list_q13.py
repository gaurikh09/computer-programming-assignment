# program to return numbers which are repearting
# Input
n = 4
arr = [1, 2, 1, 3, 4, 3]

# List to store the repeating numbers
repeating = []

# Loop through the array
for i in range(len(arr)):
    val = abs(arr[i])  # Get the absolute value of the current element
    
    # Check if the position corresponding to this value is already negative
    if arr[val - 1] < 0:
        repeating.append(val)  # If negative, it means this number is repeating
    else:
        arr[val - 1] = -arr[val - 1]  # Otherwise, mark it as visited by negating

# Print the repeating numbers
print(repeating[0], repeating[1])  # Output: 1 3
