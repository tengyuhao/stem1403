"""
set method - issubset()
"""

A = {1, 2, 3, 4}
B = {4, 5, 6, 7}

result = A.issubset(B)
print(result)
print()

A = {1, 2, 3, 4}
B = {1, 2}

result = B.issubset(A)
print(result)
print()

A = {1, 2, 3, 4}
B = {1, 2, 3, 4}

result = B.issubset(A)
print(result)
print()

result = A.issubset(B)
print(result)
print()

