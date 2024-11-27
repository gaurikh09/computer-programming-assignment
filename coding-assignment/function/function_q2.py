# fibonacci series
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    
    return fib_sequence

# Example usage
n = 5
print(fibonacci(n))  # Output: [0, 1, 1, 2, 3]
