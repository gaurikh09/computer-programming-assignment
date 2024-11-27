# tuple of maximum sum

tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
max_sum_tuple = max(tuples_list, key=lambda x: sum(x))

print(max_sum_tuple)
