# largest element in a list
def find_largest_element(arr):
    if len(arr) == 0:
        return None  # Return None if the list is empty
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Example usage
arr = [10, 20, 4, 45, 99]
print(find_largest_element(arr))  # Output: 99
