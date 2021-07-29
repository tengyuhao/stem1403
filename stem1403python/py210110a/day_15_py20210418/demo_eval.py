"""
eval()
"""

# 1. evaluate an expression
# string -> expression
# return value


# 1+2*3-6/2

def add(a, b):
    return a + b


res = eval('1+2*3-6/2')
print(res)

# expression of string comes from keyboard (CLI input)
# from Entry (GUI input)

expr = input('Input your expression')
result = eval(expr.strip())
print(result)