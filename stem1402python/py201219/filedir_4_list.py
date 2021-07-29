"""
list dirs and files

listrdir()
"""

import os

result = os.listdir()
print(type(result), "\n", result)

for item in result:
    print(item)

print("=============================")

result2 = os.listdir("../py201128")
print(result2)

for item in result2:
    print(item)
