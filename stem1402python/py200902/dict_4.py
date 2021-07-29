"""
mixed keys

immutable keys of datatype
different datatypes

how to access info of an inity
"""

# abstract example
dict4 = {
    1: "value",
    '1': "value2",
    'name': "Peter"  # ,
    # 1.23 : 'v2'
}


print(dict4)

# concrete example
# employee in company
# employee id -> empid
person_profile = {
    'empid': '0001',
    'name': 'Peter',
    'ismanager': True,
    1: 'availabe',
    2: 'long-term'
}

# question: how to access info of Peter
print(person_profile['empid'])
print(person_profile['name'])
print(person_profile['ismanager'])
print(person_profile[1])
print(person_profile[2])

list1 = [1, 2, 3]
print(list1[1])


