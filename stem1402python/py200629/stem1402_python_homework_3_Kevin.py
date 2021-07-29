"""
stem1402_python_homework_3_Kevin
[Homework] 1-7
1. Write a Python function to find the Max of three numbers.
2. Write a Python function to sum all the numbers in a list.
3. Write a Python function to multiply all the numbers in a list.
4. Write a Python program to reverse a string.
5. Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.
6. Write a Python function to check whether a number is in a given range.
7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
"""


# 1. Write a Python function to find the Max of three numbers.


def max_3_numbers(x, y, z):
    biggest_number = x
    if biggest_number < y:
        biggest_number = y
    if biggest_number < z:
        biggest_number = z
    return biggest_number


n1 = 10
n2 = 60
n3 = 30
result = max_3_numbers(n1, n2, n3)
print("Question 1. The Max of {}, {} and {} is {}.".format(n1, n2, n3,result))


# 2. Write a Python function to sum all the numbers in a list.
list1 = [5, 10, 50]


def adding(list1):
    result = 0
    for i in list1:
        result = result + i
    return result


# adding n1, n2 and n3
result = adding(list1)
# print("adding n1:{n1} and n2:{n2} = {res}".format(n1=n1, n2=n2, res=result))
print("Question 2. {n1} + {n2} + {n3} = {res}".format(n1=list1[0], n2=list1[1], n3=list1[2], res=result))


# 3. Write a Python function to multiply all the numbers in a list.

list2 = [5, 10, 15]


def multiple(list2):
    result = 1
    # multiple n1, n2 and n3
    for i in list2:
        result = result * i
    return result


result = multiple(list2)
print("Question 3. {n1} x {n2} x {n3} = {res}".format(n1=list2[0], n2=list2[1], n3=list2[2], res=result))


# 4. Write a Python program to reverse a string.
print("===== Question 4. =====")
str1 = 'Hello!'
print("Original str:", str1)

# for char in str1:
#     print(char, end="\t")

new_str = ''
for i in range(-1, -7, -1):
    # print(str1[i], end="")
    new_str += str1[i]

print("New str:", new_str)
print("========= End =========")


# 5. Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.


def factorial(num1):
    result_factorial = 1
    for i in range(1, num1 + 1):    # range(1, 7)
        result_factorial = result_factorial * i     # rf = rf * 1, rf = rf * 2, ...
    return result_factorial


print("Question 5. The result is {}".format(factorial(6)))


# 6. Write a Python function to check whether a number is in a given range.


def check_range(number, lowest, highest):
    if number > lowest:
        if number < highest:
            result = True
    else:
        result = False
    return result


print("Question 6. The condition is {}.".format(check_range(666, 300, 800)))


# 7. Write a Python function that accepts a string and
# calculate the number of upper case letters and lower case letters.
# 1.
def number_of_uppercase_and_lowercase(str1):
    result1 = 0
    result2 = 0
    for letters in str1:
        if letters in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            result1 += 1

        if letters in 'abcdefghijklmnopqrstuvwxyz':
            result2 += 1
    return result1, result2


print(number_of_uppercase_and_lowercase("abcABC"))


# 2.
def number_of_uppercase_and_lowercase(str1):
    result1 = 0
    result2 = 0
    for letters in str1:
        if letters >= 'a' and letters <='z':
            result1 += 1

        if letters >= 'a' and letters <='z':
            result2 += 1
    return result1, result2


print(number_of_uppercase_and_lowercase("abcdefgABCDEFG"))

# 3. My idea.


def number_of_uppercase_and_lowercase(str1):
    result1 = 0
    result2 = 0
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    abc = 'abcdefghijklmnopqrstuvwxyz'

    for letters in str1:
        # for lowercase
        if letters in ABC:
            result1 += 1

        # for uppercase
        if letters in abc:
            result2 += 1
    return result1, result2


print(number_of_uppercase_and_lowercase('WEFIFIEWYFWBIAIFbuflbhvwilbhwvbilewibh'))




