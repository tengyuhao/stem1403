"""
set operation - set union
"""

A = {1, 2, 3, 4}
B = {4, 5, 6, 7}
print(f"Set A: {A}")
print(f"Set A: {B}")

result = A & B
print(f"Result set : {result}, {type(result)}")

result = A.intersection(B)
print(f"Result set : {result}")

result = B.intersection(A)
print(f"Result set : {result}")

