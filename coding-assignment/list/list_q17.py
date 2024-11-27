# program to shift elements left by k positions

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
k = int(input("Enter the number of positions to shift: "))
k %= len(lst)
shifted_list = lst[k:] + lst[:k]
print("Shifted list:", shifted_list)
