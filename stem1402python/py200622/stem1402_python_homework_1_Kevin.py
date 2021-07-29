"""
Homework stem1402
1. Write a Python function to find the Max of three numbers.
2. Write a Python function to sum all the numbers in a list.
"""

# 1. Write a Python function to find the Max of three numbers.
list1 = [55, 100, 66]   # 100 is the biggest


def number_final(list1):
    biggest_number = list1[0]
    for num in list1:
        if biggest_number < num:
            biggest_number = num
    return biggest_number


print("The Max of three numbers is {}".format(number_final(list1)))


# 2. Write a Python function to sum all the numbers in a list.
list1 = [55, 66, 77, 88, 666]


def sum_final(list1):
    sum = 0
    for num in list1:
        sum += num
    return sum


print("The Max of three numbers is {}".format(sum_final(list1)))




