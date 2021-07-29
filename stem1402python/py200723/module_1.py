"""
Module a file containing python statement and definitions

- global variables (definition)
- constant (definition)
- function (definition)
- class (definition)


module is a python file
"""

import py200723.mymodule as mymodule

# from py200723.mymodule import foo3
# from py200723.mymodule import foo2, foo1

# foo3()

# foo1()
# foo2()

import math
print(math.pi)

from math import pi
print(pi)

from math import *
print(pi)
print(abs(-100))

import sys
print(sys.path)

for path in sys.path:
    print(path)

"""
['/Users/kevinteng/PycharmProjects/stem1402python/py200723', '/Users/kevinteng/PycharmProjects/stem1402python', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/kevinteng/Library/Python/3.7/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages']
/Users/kevinteng/PycharmProjects/stem1402python/py200723
/Users/kevinteng/PycharmProjects/stem1402python
/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload
/Users/kevinteng/Library/Python/3.7/lib/python/site-packages
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages
"""

# list all contents(names) in a module
items = dir(mymodule)

for item in items:
    print(item)
