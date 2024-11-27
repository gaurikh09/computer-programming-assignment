# program to remove negativenumbers
# Input array
arr = [1, -1, 3, 2, -7, -5, 11, 6]

# Auxiliary lists for positive and negative numbers
positive = []
negative = []

# Step 1: Separate positive and negative numbers
for num in arr:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

# Step 2: Overwrite the original array
for i in range(len(positive)):
    arr[i] = positive[i]

for i in range(len(negative)):
    arr[len(positive) + i] = negative[i]

# Output the modified array
print(arr)  # Output: [1, 3, 2, 11, 6, -1, -7, -5]
