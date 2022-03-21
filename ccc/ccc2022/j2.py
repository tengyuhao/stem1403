N = int(input())
totalL = []
count = 0

for i in range(N):
    point = int(input())
    fautes = int(input())
    total = point * 5 - fautes * 3
    totalL.append(total)

for i in totalL:
    if i > 40:
        count += 1

if count == N:
    print(f"{N}+")
else:
    print(count)