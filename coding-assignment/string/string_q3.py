# to check if words are anamgram or not
# Input strings
s1 = "geeks"
s2 = "kseeg"
# Check if lengths are the same
if len(s1) != len(s2):
    print(False)
else:
    # Sort both strings and compare
    if sorted(s1) == sorted(s2):
        print(True)
    else:
        print(False)
