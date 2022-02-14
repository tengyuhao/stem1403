"""
CCC J5 - 2021
Modern Art
"""


def process(color, num):
    global ArtL
    if color == 'R':
        for i2 in range(len(ArtL)):

            if i2 == int(num) - 1:
                for i3 in range(len(ArtL[i2])):
                    if ArtL[i2][i3] == True:
                        # print(ArtL[i2][i3])
                        ArtL[i2][i3] = False
                        # print(ArtL[i2][i3])
                        # print(ArtL)
                    elif ArtL[i2][i3] == False:
                        ArtL[i2][i3] = True
                        # print("1223")
    elif color == 'C':
        num = int(num)
        for i2 in range(len(ArtL)):
            if ArtL[i2][num - 1] == True:
                # print(ArtL[i2][i3])
                ArtL[i2][num - 1] = False
                # print(ArtL[i2][i3])
                # print(ArtL)

            elif ArtL[i2][num - 1] == False:
                ArtL[i2][num - 1] = True
                # print("1223")


M = int(input())
N = int(input())
ArtL = [[False for i in range(N)]for i in range(M)]
# print(ArtL)
K = int(input())
for i in range(K):
    info = input()
    color, num = info.split(" ")
    process(color, num)
# print(ArtL)
count = 0
for i in ArtL:
    for i2 in i:
        if i2 == True:
            count += 1
print(count)