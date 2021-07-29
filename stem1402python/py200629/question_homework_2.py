"""
[Homework] 1-4
1. Write a Python function to find the Max of three numbers.
2. Write a Python function to sum all the numbers in a list.
3. Write a Python function to multiply all the numbers in a list.
4. Write a Python program to reverse a string.
5. Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.
6. Write a Python function to check whether a number is in a given range.
7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
"""


"""
4.
'a', 'b', 'c', 'd', 'e', 'f',
"""

str1 = 'abcdef'
print("original str: ", str1)

# for char in str1:
#     print(char, end="\t")

new_str = ''
for i in range(-1, -7, -1):
    # print(str1[i], end="")
    new_str += str1[i]

print("new str: ", new_str)
