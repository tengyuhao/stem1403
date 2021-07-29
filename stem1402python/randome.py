"""
randome test
"""

import random
x = random.randint(1, 100)
i = 0
while i < 100:
    y = int(input("Please input an number:"))
    if x == y:
        print("Bingo")
        break
    elif y < x:
        print("Too small")
    else:

        print("Too big")

# Intelligent
import random
x = random.randint(1, 100)
i = 0
for i in range(1,5):
    break
