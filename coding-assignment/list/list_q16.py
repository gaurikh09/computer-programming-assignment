# program to find the longest element in a list

lst = [x for x in input("Enter elements separated by space: ").split()]
longest = lst[0]
for elem in lst:
    if len(elem) > len(longest):
        longest = elem
print("Longest element:", longest)
