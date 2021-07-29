"""
dictionary keys()
"""

mydict = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e'
}
print("Before:", mydict)

for item in mydict.keys():
    print(item, type(item))

# keys()
result = mydict.keys()
print(result, type(result))

# dict_keys -> list, extract as a list
result2 = list(mydict.keys())
print(result2, type(result2))

"""
result:
Before: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
1 <class 'int'>
2 <class 'int'>
3 <class 'int'>
4 <class 'int'>
5 <class 'int'>
dict_keys([1, 2, 3, 4, 5]) <class 'dict_keys'>
[1, 2, 3, 4, 5] <class 'list'>

Process finished with exit code 0
"""

