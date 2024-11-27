# program to return number of zeroes present in an array
# Input
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
n = len(arr)

# Initialize a count variable
count_of_zeros = 0

# Iterate through the array
for i in range(n):
    if arr[i] == 0:
        count_of_zeros = n - i  # Remaining elements are all 0's
        break  # Stop further iteration since we found all 0's

# Output the count
print(count_of_zeros)  # Example Output: 3
