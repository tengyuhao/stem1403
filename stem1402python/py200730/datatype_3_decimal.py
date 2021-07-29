"""
decimal module

When to use Decimal instead of float?
1. making financial application that need exact decimal representation
2. to control the level of precision required
3. to implement the notion of significant decimal places
4. when we want the operations to be carried out like we did at school
"""

# import decimal
from decimal import Decimal

print(Decimal(1.1))
print(Decimal(2.2))
print(Decimal(3.3))
print()


# string literal
print(Decimal('1.1'))
print(Decimal('2.2'))
print()

result = Decimal('1.1') + Decimal('2.2')
print(result, type(result))

result = Decimal('1.1') - Decimal('2.2')
print(result, type(result))

result = Decimal('1.2') * Decimal('2.5')
print(result, type(result))

result = Decimal('1.2') * Decimal('2.50')
print(result, type(result))

result = Decimal('1.2') * Decimal('2.500')
print(result, type(result))

result = Decimal('1.1') / Decimal('2.2')
print(result, type(result))

a = Decimal('1.1')
b = Decimal('2.2')
c = Decimal('3.3')
if a + b == c:
    print(True)

else:
    print(False)