"""
datatype conversion
int(), float(), str()  built-in function
"""

# case 1. string -> float
str1 = '1.23'
print(str1, type(str1))

# print("subtotal = ", str1 * 2)

float1 = float(str1)
print(float1, type(float1))

print("===========")

# case 2. string -> int
str1 = '99'
print(str1, type(str1))

int1 = int(str1)
print(int1, type(int1))

print("===========")

# case 2b. string -> int  # error
# str1 = 'abc'
# str1 = '1.2'
# print(str1, type(str1))

# int1 = int(str1)
# print(int1, type(int1))


# case 3. int -> float
int1 = 88
print(int1, type(int1))

float1 = float(int1)
print(float1, type(float1))
print("===========")


# case 3. float -> int
float1 = 88.0
print(float1, type(float1))

int1 = int(float1)
print(int1, type(int1))
print("===========")

# case 3b. float -> int
float1 = 88.999
print(float1, type(float1))

int1 = int(float1)
print(int1, type(int1))
