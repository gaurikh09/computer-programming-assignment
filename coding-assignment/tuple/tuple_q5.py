#Remove a key from a dictionary if it exists.
def delete_key(d, key):
    d.pop(key, None)
    return d

# Example
d = {'a': 1, 'b': 2, 'c': 3}
print(delete_key(d, 'b'))  # Output: {'a': 1, 'c': 3}
