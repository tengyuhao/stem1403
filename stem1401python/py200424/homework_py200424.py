"""
homework
"""

# For example
value_1 = 2020
print("value_1 = ", type(value_1))
# Result is value_1 =  <class 'int'>

value_2 = 6.66
print("value_2 = ", type(value_2))
# Result is value_2 =  <class 'float'>


num = 9
result = isinstance(num, int)
print(result)   # True


"""
7. How can I change a floating point number 
to a string and a string to an integer.
"""
# float -> string
float_1 = 0.99
string_1 = str(float_1)
print(string_1, type(string_1))     # 0.99 <class 'str'>


# string -> int
string_2 = "100"
int_1 = int(string_2)
print(int_1, type(int_1))       # 100 <class 'int'>
