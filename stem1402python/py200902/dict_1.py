"""
dictionary is a collection datatype

1. unordered collection
2. {}
3. item is a key:value pair, entry
4. Unique key
5. one key has only one value


"""

# how to create a dictionary?
dict1 = {
    1: "value1",
    2: "value2",
    3: "value3",
    # ...
    1000: "value1000"
}

print(dict1)

# why
# every key in the dictionary wills be hashable
# for look up a piece of data within a constant time
# iteration
# for in range(1000)
#     print(i)

# to iterate over a dictionnary
for key in dict1:
    print(key, dict1[key])
