"""
2. Write a Python function to sum all the numbers in a list.
"""

# step 1
# list1 = [1, 2, 3, 4, 5]
#
# sum = 0
# for num in list1:
#     sum += num
#
# print(sum)


# step 2. generic
def get_sum(mylists):
    """
    calculate the sum of the lists items 
    :param mylists: a list
    :return: the sum
    """
    sum_list = 0
    for num in mylists:
        sum_list += num

    return sum_list


# input
list_input = [1, 2, 3, 4, 5, 6, 7]
# list_input = []
print("original list is {}".format(list_input))

# process
# get the summary
sum = 0
sum = get_sum(list_input)

# output
print("sum of the list is {}".format(sum))


# step 3. test

# step 4. optimize
# readability
# syntax, logic error
#

