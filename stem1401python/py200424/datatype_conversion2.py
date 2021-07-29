"""
datatype conversion of collection
list(), tuple(), dict(), set()
"""

# case 1. list to tuple
list1 = [1, 2, 3]
print(list1)
print(tuple(list1))

# case 2. tuple to list
tuple1 = (1, 2, 3)
print(tuple1)
print(list(tuple1))

# case 3. str(tuple) to list
str1 = 'hello'
print(list(str1))
print(list('hello'))

print()

# case 4. list to dictionary
list2 = [["MON", "Monday"], ["TUE", "Tuesday"]]
print(dict(list2))

# case 5. tuple to dictionary
tuple2 = (("MON", "Monday"), ("TUE", "Tuesday"))
print(dict(tuple2))

print()

# case 6. dictionary to list
dict1 = {
    'MON': 'Monday',
    'TUE': 'Tuesday'
}
print(list(dict1))

# case 7. dictionary to tuple
dict1 = {
    'MON': 'Monday',
    'TUE': 'Tuesday'
}
print(tuple(dict1))

print()

# case 8. list to set
list1 = [1, 2, 3]
print(set(list1))

list1 = [1, 1, 2, 2, 3, 3]
print(set(list1))

# case 9. tuple to set
tuple1 = (1, 2, 3)
print(set(tuple1))

tuple1 = (1, 1, 2, 2, 3, 3)
print(set(tuple1))

print()

# case 10. set to list
set1 = {1, 2, 3}
print(list(set1))

# case 11. set to tuple
set1 = {1, 2, 3}
print(tuple(set1))


