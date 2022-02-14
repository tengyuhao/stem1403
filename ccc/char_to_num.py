"""
character to number(integer)

number to character
"""

# case 1.
c = 'A'
result = ord(c)
print(result)


# case 2.
# num =111
# result = chr(num)
# print(result)
#
# num -= 2
# # print(chr(num))


# case 3.
for i in range(97, 97+26):
    print(chr(i), i)

# print(chr(97+26-1), ord(97+26-1))

