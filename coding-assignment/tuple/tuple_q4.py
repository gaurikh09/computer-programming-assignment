# merge two tuple
list1 = input("Enter first list elements separated by spaces: ").split()
list2 = input("Enter second list elements separated by spaces: ").split()

result_tuple = tuple(zip(list1, list2))
print("Tuple of pairs:", result_tuple)
