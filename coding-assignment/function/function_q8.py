# pallindromre checker
def is_palindrome(s):
    return s == s[::-1]

# Example usage
s = "madam"
print(is_palindrome(s))  # Output: True
