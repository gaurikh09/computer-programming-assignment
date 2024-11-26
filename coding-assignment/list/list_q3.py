# progtram to find if b is a subset of a or not
def is_subset(a, b):
    freq = {}
    for num in a:
        freq[num] = freq.get(num, 0) + 1
    for num in b:
        if freq.get(num, 0) == 0:  # Element not found
            return "No"
        freq[num] -= 1  

    return "Yes"  # All elements of b[] are found in a[]
