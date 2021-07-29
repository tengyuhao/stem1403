"""

"""

mydict2 = {
    's001': 97,
    's002': 94,
    's003': 87,
    's004': 90,
    's005': 94
}

# step 1. get values
result = list(mydict2.values())

# step 2. remove if applicable
# list -> set
set_value = set(result)
result = list(set_value)
print(result)
