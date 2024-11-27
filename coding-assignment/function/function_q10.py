# sum of a number 
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Example usage
n = 12345
print(sum_of_digits(n))  # Output: 15
