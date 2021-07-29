"""
set method - issuperset()
"""

A = {1, 2, 3, 4}
B = {4, 5, 6, 7}

result = A.issuperset(B)
print(result)
print()

A = {1, 2, 3, 4}
B = {1, 2}

result = B.issuperset(A)
print(result)
print()

A = {1, 2, 3, 4}
B = {1, 2, 3, 4}

result = B.issuperset(A)
print(result)
print()

result = A.issuperset(B)
print(result)
print()

