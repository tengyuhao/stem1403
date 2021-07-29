"""

"""

# 1X2X3X4X5X6X7X8X9X10

prod = 1
for i in range(1, 11):
    prod *= i
print(prod)
print(int(prod/5/8))

# 1X2X3X4X6X7X9X10
# missing 5 and 8

prod = 1
for i in range(1, 11):
    if i == 5 or i == 8:
        continue
    prod *= i

print(prod)


