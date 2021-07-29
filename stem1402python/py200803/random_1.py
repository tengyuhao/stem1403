"""
random

random seed
"""

import random

# randrange(n)
# 0..n-1
for i in range(100):
    a = random.randrange(6)
    # print(f"Random number is {a}")
print()

for i in range(100):
    a = random.randrange(1, 6)
    # print(f"Random number is {a}")
print()

# randint(startnum, stopnum)
for i in range(100):
    a = random.randint(1, 6)
    # print(f"Random number is {a}")


# choice()
mylist = ['White','Green','Blue','Golden','Orange']
mylist = ('White','Green','Blue','Golden','Orange')
for i in range(10):
    a = random.choice(mylist)
    print(f"Chosed random item is {a}")


str1 = 'abcdefgh'
for i in range(50):
    a = random.choice(str1)
    print(f"Chosed random item is {a}")


# shuffle(x)
mylist = ['White','Green','Blue','Golden','Orange']
# a = random.shuffle(mylist)
# print(a, type(a))
for i in range(5):
    random.shuffle(mylist)
    print(mylist)

