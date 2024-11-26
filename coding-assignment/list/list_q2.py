# tofind an element and return its index
def find_element_index(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Return the index of the first occurrence
    return -1  # Return -1 if x is not found
