# remove duplicates from a list
def remove_duplicates(arr):
    unique_list = []
    for element in arr:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

# Example usage
arr = [1, 2, 2, 3, 4, 3, 5]
print(remove_duplicates(arr))  # Output: [1, 2, 3, 4, 5]
