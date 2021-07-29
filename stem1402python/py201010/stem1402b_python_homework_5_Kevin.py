"""
1. Write a Python program to sum all the items in a dictionary.
2. Write a Python program to multiply all the items in a dictionary.
3. Write a Python program to get the maximum and minimum value in a dictionary.
5. Write a Python program to remove duplicates from Dictionary.
"""

# Question 1.
mydict1 = {
    's001': 97,
    's002': 94,
    's003': 87,
    's004': 90,
    's005': 94
}
res = 0
for item in mydict1.values():
    print(item, type(item))
    res = item + res

print(res)


# Question 2.
print("Question 2.")
mydict1 = {
    's001': 97,
    's002': 94,
    's003': 87,
    's004': 90,
    's005': 94
}

res = 1
for item in mydict1.values():
    print(item, type(item))
    res = item * res

print(res)

# Question 3.
mydict1 = {
    's001': 97,
    's002': 94,
    's003': 87,
    's004': 90,
    's005': 94
}

import operator

sorted_order_number = sorted(mydict1.items(), key=operator.itemgetter(1))
print(sorted_order_number[0][1], sorted_order_number[-1][1])

# Question 4.
mydict1 = {
    's001': 97,
    's002': 94,
    's003': 87,
    's004': 90,
    's005': 94
}
tuple_mydict1 = set(mydict1.values())
print(tuple_mydict1)

# 4.
mydict = {1: 3, 5: 3, 8: 4, 11: 8, 4: 6, 10: 8}
mydict_copy = {}
for i in mydict.items():
    if i[1] not in mydict_copy.values():
        mydict_copy[i[0]] = i[1]
print(mydict_copy)


