# to see the peak element
def has_peak_element(arr):
    n = len(arr)
    if n == 0:
        return False  # Empty array has no peak
    for i in range(n):
        if (i == 0 or arr[i] >= arr[i-1]) and (i == n-1 or arr[i] >= arr[i+1]):
            return True  # A peak element exists
    return False  # This case won't occur with valid inputs
