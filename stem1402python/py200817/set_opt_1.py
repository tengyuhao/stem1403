"""
set operation - set union
"""

A = {1, 2, 3, 4}
B = {4, 5, 6, 7}

result = A | B
print(result, type(result))

result = A.union(B)
print(result, type(result))

result = B.union(A)
print(result, type(result))

