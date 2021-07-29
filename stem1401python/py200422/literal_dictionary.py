"""
literal dictionary
"""

my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4"
}

# 1 key 1 value, key must be unique
my_dict2 = {
    "key1": "value1",
    "key2": "value1",
    "key3": "value2",
    "key4": "value2"
}


# the type of key
my_dict3 = {
    1: "value1",
    2: "value1",
    3: "value2",
    4: "value2"
}
print(my_dict3)


# mix type of keys
my_dict4 = {
    1: "value1",
    2: "value1",
    '3': "value2",
    '4': "value2"
}
print(my_dict4)

# the type of value varies
my_dict5 = {
    1: 1.23,
    2: 20,
    3: True,
    4: [1, 2, 3]
}
print(my_dict5)



