
"""

    -
if i == 0:
    +
"""
put = input()
list1 = put.split(" ")
# list1 = [3, 10, 12, 5]

i1 = []
i2 = []
i3 = []
i4 = []
i5 = []
init = 0
res = 0

for i in range(4):
    if i == 0:
        i1.append(0)

    res += int(list1[i])
    i1.append(res)
print(i1)
i1new = i1

i2new = i2
i2.reverse()
res = 0
for i in range(3):
    if i == 0:
        i2.append(i1[1])
        i2.append(0)
    res += int(list1[i+1])
    i2.append(res)

print(i2)
i2new = i2
i2.reverse()

res = 0
for i in range(2):
    if i == 0:
        i3.append(i1[2])
        i3.append(i2[-3])
        i3.append(0)
    res += int(list1[i+2])
    i3.append(res)

print(i3)

i3new = i3
i3.reverse()

res = 0
for i in range(1):
    if i == 0:
        i4.append(i1[3])
        i4.append(i2[1])
        i4.append(i3[1])
        i4.append(0)
    res += int(list1[i+3])
    i4.append(res)

print(i4)
i4.reverse()

i5.append(i1[4])
i5.append(i2[0])
i5.append(i3[0])
i5.append(i4[0])
i5.append(0)
# ====
print(i5)

# print(i2)
