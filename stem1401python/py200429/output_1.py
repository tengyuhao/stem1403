"""
syntax
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
"""

# *objects
print(1)
print(1, 2)
print(1, 2)
print(1, 2, 'mystr')
print(1, 2, 'mystr', 1, 2, 'mystr')

print("------")

# sep=' '
print(1, 2, 'mystr', 1, 2, 'mystr', sep=',,')

# end='\n'
print("------")
print(1, end='\t')
print(2, end='\t')
print(3, end='\t')
print(4, end='\t')
print(5, end='\t')
print(6, end='\t')
print(7)
print("------")

print("------")
print(1, end='&&')
print(2, end='&&')
print(3, end='&&')
print(4, end='&&')
print(5, end='&&')
print(6, end='&&')
print(7)
print("------")
