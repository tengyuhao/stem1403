"""
3. Listing all combination for a given set of characters (10’)
3.列出给定字符集的所有组合
Description:
You are asked to write your idea in text or a diagram to describe how to implement it.
You may write some pseudo-code instead of real code.
Coding is optional for STEM
"""
abc = 'abc'

"""
I want to print like this!!!
abc
acb
bac
bca
cab
cba
"""

# i think I will continue write the code, and observe the code continued.
# so it's my idea. And this is just one example.
for i in range(3):
    for i1 in range(1):
        print(abc[i1], end="")
    for i2 in range(1):
        print(abc[i2-2], end="")

print("")
