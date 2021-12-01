"""
j4 2021
Resources: 0.523s, 15.57 MB
Final score: 9/15 (4.2/7 points)
"""

resA = 0
resB = 0
res = 0
L = 0
M = 0
S = 0
book = list(input())
for i in book:
    if i == "L":
        L += 1
    elif i == "M":
        M += 1
    elif i == "S":
        S += 1

# section A, B, C
sA = book[:L]
sB = book[L:L+M]
# sC = book[S:]

for i2 in sA:
    if i2 == "L":
        L -=1
        # print(L) correct
    elif sA == "M":
        resA += 1

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
# print(sA)
# print(sB)
# print(sC)
