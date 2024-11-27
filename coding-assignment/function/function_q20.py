# number is armstrong or not
def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** n
    return total == num

# Example usage
num = 153
print(is_armstrong(num))  # Output: True

num = 123
print(is_armstrong(num))  # Output: False
