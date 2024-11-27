ilter tuples where the sum of elements is greater than a given value.
def filter_tuples(tpl, threshold):
    return tuple(t for t in tpl if sum(t) > threshold)

# Example
print(filter_tuples(((1, 2), (3, 4), (1, 1)), 4))  # Output: ((3, 4),)
