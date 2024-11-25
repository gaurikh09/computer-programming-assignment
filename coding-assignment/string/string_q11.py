# program to rotate a string 
s1 = "amazon"
s2 = "azonam"
rotated_anticlockwise = s1[2:] + s1[:2]
rotated_clockwise = s1[-2:] + s1[:-2]
if rotated_anticlockwise == s2 or rotated_clockwise == s2:
  print(True)
else:
  print(False)
else:
  print(False)
