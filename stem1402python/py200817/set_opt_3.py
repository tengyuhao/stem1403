"""
set operation - set diffenrence
"""

A = {1, 2, 3, 4}
B = {4, 5, 6, 7}
print(f"Set A: {A}")
print(f"Set A: {B}")

result = A - B
print(f"Result set A - B: {result}, {type(result)}")

result = A.difference(B)
print(f"Result set : {result}")

result = B - A
print(f"Result set B - A: {result}, {type(result)}")

result = B.difference(A)
print(f"Result set : {result}")

