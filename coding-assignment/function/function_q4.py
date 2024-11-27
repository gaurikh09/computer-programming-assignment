# program to check number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
n = 7
print(is_prime(n))  # Output: True
