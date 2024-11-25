#Replace all vowels in a string with '*'.
def replace_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join('*' if char in vowels else char for char in s)

# Example
print(replace_vowels("hello world"))  # Output: "h*ll* w*rld"
