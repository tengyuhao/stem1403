"""
Homework 4 - Kevin
To calculate the n th item of a Fibonacci sequence
"""

"""
1, 1, 2, 3, 5, 8, 13, 21, 34, ......
"""


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n < 1:
        return "error"
    else:
        return fibonacci(n-1) + fibonacci((n-2))


n = input("Please enter one number to calculate the n th item of a Fibonacci sequence: ")
n = int(n)

for i in range(1, n+1):
    print(fibonacci(i), end="\t")


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



