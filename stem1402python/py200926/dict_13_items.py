"""
dictionary items()
item = key:value
dictionary contains multiple items
"""

mydict = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e'
}
print(mydict)

# iterable
for item in mydict.items():
    print(item, type(item))
    print(item[0], item[1])

# items()
result = mydict.items()
print(result, type(result))

# extract as a list
result2 = list(mydict.items())
print(result2, type(result2))


for item in result2:
    print(item, type(item))
