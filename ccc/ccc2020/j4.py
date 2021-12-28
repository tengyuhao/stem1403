"""
J4 2020

"""
T = input()
S = input()

res = None
# print(res)

# generate all forms of string
cyclic = []
n = len(S)

for i in range(n):

    S = S[1:] + S[0]
    cyclic.append(S)

# print(cyclic)
res = "no"
for i in cyclic:
    if i in T:
        res = "yes"
        break

print(res)
