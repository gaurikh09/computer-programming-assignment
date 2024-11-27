# count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage
s = "Hello World"
print(count_vowels(s))  # Output: 3
