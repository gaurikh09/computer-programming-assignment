#program to reverse a string
def reverse_string(s: str) -> str:
    return s[::-1]  # Slicing to reverse the string

# Examples
print(reverse_string("Geeks"))  # Output: "skeeG"
print(reverse_string("for"))    # Output: "rof"
print(reverse_string("a"))      # Output: "a"
