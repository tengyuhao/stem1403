N = int(input())
num = 0
last = None
listABC = []
for i in range(N):
    abc = list(input())
    listABC.append(abc)
print(listABC)

for i in listABC:
    num = 0
    for i2 in i:
        if i2 != last:
            pass
            # print(num)
            # print("!=")
        elif i2 == last:
            num += 1
            # print("==")

        else:
            pass
        last = i2

        # print(num)

    print(f"{last} {num}")
