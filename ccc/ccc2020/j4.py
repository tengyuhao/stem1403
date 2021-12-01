"""

"""
S = input()
T = input()
res = S in T
# print(res)

# generate all forms of string
cyclic = []
n = len(S)

for i in range(n):

    S = S[1:] + S[0]
    cyclic.append(S)

print(cyclic)
for i in cyclic:
    if T in i == True:
        print("yes")
    else:
        print("no")
        break
