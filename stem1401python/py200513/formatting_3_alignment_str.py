"""
String formatting with format()
"""

# string padding with left alignment
print("|{:5}|".format("cat"))


# string padding with right alignment
print("|{:>5}|".format("cat"))


# string padding with center alignment
print("|{:^5}|".format("cat"))
print("|{:^8}|".format("cat"))
print("|{:^10}|".format("cat"))
print("|{:^12}|".format("cat"))

# 12-len(str) % 2 == 1, white space on the left < that on the right

# string padding with center alignment
# and '*' padding character
print("{:*^5}".format("cat"))
print("{:=^5}".format("cat"))
