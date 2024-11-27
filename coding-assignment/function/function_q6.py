# find largest element in the list
def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Example usage
arr = [3, 5, 7, 2, 8, 6]
print(find_largest(arr))  # Output: 8
