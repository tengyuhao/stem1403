"""
alignment for numbers
The operators <, ^, > and = are used for alignment
when assigned a certain width to the numbers

Number formatting with alignment
Type   Meaning
<  Left aligned to the remaining space
^  Center aligned to the remaining space
>  Right aligned to the remaining space
=  Forces the signed (+) (-) to the leftmost position
"""

# integer
print("{:8d}".format(12))
print("{:8.3f}".format(12.2346))
print()

print("{:>8d}".format(12))
print("{:>8.3f}".format(12.2346))
print()

print("|{:<8d}|".format(12))
print("|{:<8.3f}|".format(12.2346))
print()

print("|{:^8d}|".format(12))
print("|{:^8.3f}|".format(12.2346))
print()

print("{:=8.3f}|".format(-12.3456))
print("{:=9.3f}|".format(-12.2346))
print("{:=10.3f}|".format(-12.3456))
print("{:=11.3f}|".format(-12.2346))
print()

print("{:=+11.3f}|".format(12.2352))
print("{:=+8.3f}|".format(12.324))
print("{:=+16.3f}|".format(12.324))
print()

print("{:+=16.3f}|".format(12.2352))
print("{:*=16.3f}|".format(12.324))
