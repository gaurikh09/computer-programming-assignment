# program to validate an IP address
s = "222.111.111.111"

# Split the string by the dot
parts = s.split(".")

# There must be exactly 4 parts
if len(parts) != 4:
    print(False)
else:
    valid = True
    for part in parts:
        # Each part must be a number and should not be empty
        if not part.isdigit():
            valid = False
            break
        # Check the length of the part to avoid leading zeros
        if len(part) > 1 and part[0] == '0':
            valid = False
            break
        # Convert the part to an integer and check if it is between 0 and 255
        num = int(part)
        if num < 0 or num > 255:
            valid = False
            break
    
    print(valid)
