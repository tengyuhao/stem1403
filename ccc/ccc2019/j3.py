N = int(input())
num = 0

for i in range(N):
    abc = list(input())
    print(abc)
    for i2 in range(len(abc)):
        if abc[i2+1] != abc[i2]:
            # print(num)
            print("!=")
        elif abc[i2+1] == abc[i2]:
            num += 1
            print("==")

        else:
            break
print(num)
