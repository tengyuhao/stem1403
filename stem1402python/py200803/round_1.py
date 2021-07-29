"""
round

round()
round(number, num_decimal_places)
"""

f1 = 1.2346

res = round(f1)
print(res)

f1 = 1.4999999

res = round(f1)
print(res)

f1 = 1.5000001
res = round(f1)
print(res)


res = round(f1, 1)
print(res)

res = round(f1, 2)
print(res)

res = round(f1, 3)
print(res)

"""
homework
1.5 -> 2
"""

print("{:.3f}".format(1.2346))

