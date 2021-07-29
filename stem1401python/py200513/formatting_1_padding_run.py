"""
number padding
"""

# align to the right by default
print("{:5d}".format(12))
# print("{:5d}".format(1234567))

# leading zero
print("{:05d}".format(12))
print("{:8.3f}".format(12.23456))
print("{:08.3f}".format(12.23456))

# why?
"""
1
2
3

9
10

001
002
..
010
..
099
100

"""

# Number formatting for signed numbers
print(12.23)
print("{:+f} {:+f}".format(12.23, -12.23))

# show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))

# show space for + sign
print("{: f} {: f}".format(12.23, -12.23))

# when to use?


