# program to  find sum
def find_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Examples
arr1 = [1, 2, 3, 4]
arr2 = [1, 3, 3]

print(find_sum(arr1))  # Output: 10
print(find_sum(arr2))  # Output: 7
