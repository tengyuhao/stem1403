"""
2021 J4
资源： 0.426s, 15.64 MB
最慢一次测试的运行时间 0.121s
最终得分： 15/15 (7.0/7 points)
"""

L = 0
M = 0
# S = 0 not need
book = list(input())
for i in book:
    if i == "L":
        L += 1
    elif i == "M":
        M += 1
    # elif i == "S":
    #     S += 1
    else:
        pass

# section A, B, C
sA = book[:L]
sB = book[L:L+M]
# sC = book[S:]

resA = 0
for i2 in sA:
    if i2 == "L":
        L -= 1
        # print(L) correct
    elif i2 == "M":
        resA += 1
    # not need

resB = 0
for i3 in sB:
    if i3 == "M":
        M -= 1
    elif i3 == "L":
        resB += 1


# print(sB)
# print(resA, resB)
# print(f"{L} + {M} - {resA} - {resB}")
# print(L, M, S)
res = L + M - min(resA, resB)
print(res)
