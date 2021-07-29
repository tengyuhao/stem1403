"""
dictionary values()
"""

mydict = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'a'
}

mydict2 = {
    's001': 97,
    's002': 94,
    's003': 87,
    's004': 90,
    's005': 94
}

print("Before:", mydict)

for item in mydict.values():
    print(item, type(item))

# values()
result = mydict.values()
print(result, type(result))

# dict_values -> list, extract as a list
result2 = list(mydict.values())
print(result2, type(result2))

# result : use values(), every values in one dictionary can be a list.
# Before: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
# ['a', 'b', 'c', 'd', 'e'] <class 'list'>

# sorting
# comparison, max, min
# updating
