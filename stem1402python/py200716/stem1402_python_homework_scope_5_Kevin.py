"""
rules of global keyword

1. when creating a var inside a function, lt's local by default
2. when defining a var outside a function, it's global by default
3. you don't have to use global keyword outside
4. use global keyword to r/w a global var inside a function
5. use of global keyword outside a function has no effect
"""

# [Homework]
# 1. project3.  v1 -> v2 (update your program)
#    extend your function based on v1(or v1.1)
# menu level 1
#     adding two menu items
# under each new menu item (level 1)
#     adding two sub menu items  (level 2)

# focus on the structure and upgrade by min efforts

# 2. write programs to test if a variable inside if-block or for-block is a global var or local var
if True:
    x = 10

print(x, "is a global variable")

for i in [1, 2, 3]:
    pass

print(i-2, ",", i-1, ",", i, ", so i is a global value")



