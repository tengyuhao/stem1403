"""
sorting in ascending order
numeric : from the smallest to the biggest
string : A->Z a->z
A : 66

sorting in descending order

sorted()
keys()
"""

# sorting a dictionary
d = {'ca': 2, 'ab': 4, 'bb': 3, 'b': 1, 'aa': 0}
print("before: ", d)

# sorted() - built-in
result = sorted(d.keys())
print(result, type(result))

# convert to dictionary
# sorted_d = dict(result)
# print("after: ", sorted_d)

print("{", end="")
for key in result:
    print(f"{key}:{d[key]},", end="")
print("}")

