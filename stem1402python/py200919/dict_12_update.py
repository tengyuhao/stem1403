"""
dictionary
update()
"""

dict1 = {1:"one", 2:"three"}


# case 1. update with another dictionary
dict2 = {2:"two"}
dict1.update(dict2)
print(dict1)

dict3 = {3:"three"}
dict1.update(dict3)
print(dict1)
print()
