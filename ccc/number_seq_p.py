"""
permutation()

combination()
"""

import itertools
import math

mylist = ['a', 'b', 'c', 'd']
result = list(itertools.permutations(mylist, 4))
print(result)
print(len(result))
for case in result:
    print(''.join(case))


n = 4
r = 2
number = math.factorial(n) / math.factorial(n-r)
print(number)




