"""
R 2
R 3
W 5
S 2
S 3

R 12
W 2
R 23
W 3
R 45
S 45
R 45
S 23
R 23
W 2
S 23
R 34
S 12
S 34

"""
N = int(input())

allL = []
friendS = {}
friendS = set(friendS)
res = []

for i in range(N):
    info = input()
    indicates, friend = info.split(" ")
    t1 = [indicates, friend]
    if indicates == 'W':
        pass
    else:
        friendS.add(friend)
    allL.append(t1)

friendS = list(friendS)
friendS.sort()

print(friendS)
count = 0

for i in friendS:
    # print(i)
    init = 0
    last = 0
    for y in allL:
        vef = 1
        # count time
        if y[0] == 'W':
            count += int(y[1])-1
        elif y == allL[0]:
            pass
        else:
            count += 1

        if y[1] == i and y[0] == 'R':
            init = count
            # vef = 1
        elif y[1] == i and y[0] == 'S':
            last = count
            resa = "friend", y[1], last - init
            res.append(resa)
            vef = 0
        elif y[1] == i and vef == 1:
            resa = "friend", y[1], -1
            res.append(resa)
        else:
            pass

        print(count)

    # if resa[2] == 1:
    #     resa[2] = -1

print(res)