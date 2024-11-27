# check a number is anamgra
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage
s1 = "listen"
s2 = "silent"
print(is_anagram(s1, s2))  # Output: True
