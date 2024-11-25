# factorials of large numbers
# Input
n = 10  # Change this value for testing

# Compute factorial
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# Convert factorial to a list of digits
result = list(map(int, str(factorial)))

# Output the result
print(result)
