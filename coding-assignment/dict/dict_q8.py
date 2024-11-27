# Find keys that are unique to the first dictionary

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
unique_keys = dict1.keys() - dict2.keys()
print(unique_keys)
