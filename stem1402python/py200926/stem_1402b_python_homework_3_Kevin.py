"""
[Homework]
1. Write a Python program to check if a dictionary is empty or not.
2. Write a Python program to generate and print a dictionary that contains a number (between 1 and n)
in the form (x, x*x)
Requirement
using dictionary comprehension technique.
user input the number of items for this dictionary
e.g. User inputs 5
Expected Output : {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
3. Write a Python program to get the maximum and minimum value in a dictionary
4. review the code of demos in class
"""

# 1. Question. len()


def empty_or_not(res1):
    if res1 == 0:
        print("Empty dictionary")
    else:
        print("Not Empty dictionary")


print("Question 1.")
# Not empty list
dict1 = {1: 1}
print("dict1", dict1)
print(empty_or_not(len(dict1)))

# Empty list
dict2 = {}
print("dict2", dict2)
print(empty_or_not(len(dict2)))

print()

# 2. Question
print("Question 2.")
n = int(input("Please enter one number: "))
n = n * 2 - 1
mydict = {key: key*key for key in range(1, n+1) if key % 2 == 1}
print(mydict)

print()

# 3.
print("Question 3.")
dict1 = {1: 29,
         2: 77,
         3: 66,
         4: 2020,
         5: 5050,
         6: 778,
         7: 7}

result = list(dict1.values())
print(result, type(result))

max_num = result[0]
min_num = result[0]
for i in result:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i

print(dict1)
print("Maximum value in the dict1 is", max_num)
print("Minimum value in the dict1 is", min_num)
