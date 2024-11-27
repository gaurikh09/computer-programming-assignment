#Find the Key with the Maximum Value

my_dict = {'a': 10, 'b': 20, 'c': 15}
max_key = max(my_dict, key=my_dict.get)
print(max_key)  # Output: b (the key with the maximum value)
