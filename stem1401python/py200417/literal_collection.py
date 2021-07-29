"""
literal collection
"""

# List
# ordered, sequence of item
# allow duplicated items
# mutable

# declaring a list
list1 = [1, 2, 3, 4, 5]
list2 = [4, 2, 1, 3, 5]
list3 = [1, 2, 4, 5, 3]
print(list1)
print(list2)
print(list3)

list4 = [1, 2, 4, 3, 3]
print(list4)

list5 = [3, 3, 3, 3, 3]
print(list5)

list1[0] = list1[0] * 2
list1[1] = list1[1] * 2
list1[2] = list1[2] * 2
list1[3] = list1[3] * 2
list1[4] = list1[4] * 2
print(list1)

list6 = [1, 2, 3, 'abc', 'bcd', 'cde', True]
print(list6)

# Tuple
# ordered, sequence of item
# allow duplicated items
# immutable (unchangeable)

# declaring a tuple
tuple1 = (1, 2, 3, 4, 5, 6)
print(tuple1)

tuple2 = (3)
print(tuple2)
# (3) <=> 3
tuple2 = (3,)
print(tuple2)

tuple3 = (1, 1, 3, 3, 5, 5)
print(tuple3)

tuple4 = (1, 1, 1, 3, 5, 5)
print(tuple4)

# tuple1[0] = 10  # error


# Set
# unordered
# unique item
# unchangeable
set1 = {1, 2, 3, 4, 5, 6}
print(set1)

set2 = {1, 1, 2, 2, 3, 3}
print(set2)

set3 = {'a', 'b', 'c'}
print(set3)

# Dictionary









