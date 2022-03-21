
yes = []
no = []
nameL = []


def fun1(check):
    global yes, no
    y = input()
    y = y.split(" ")
    if check == True:
        yes.append(y)
    if check == False:
        no.append(y)


X = int(input())
for i in range(X):
    fun1(True)


Y = int(input())
if Y == 0:
    no = []
else:
    for i in range(Y):
       fun1(False)


G = int(input())
for i in range(G):
    name = input()
    name = name.split(" ")
    nameL.append(name)

count = 0


def check(i):
    global count, yes, no
    for i2 in yes:
        if i2[0] in i and i2[1] not in i:
            count += 1

    for i2 in no:
        if i2 in i and i2[1] in i:
            count += 1


for i in nameL:
    check(i)

print(count)
"""
1
ELODIE CHI
0
2
DWAYNE BEN ANJALI
CHI FRANCOIS ELODIE

3
A B
G L
J K
2
D F
D G
4
A C G
B D F
E H I
J K L

"""