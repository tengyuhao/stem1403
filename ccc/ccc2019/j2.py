"""
N symbol


input
N = for loop
n symbol,

output
n x symbol

20 min

Resources: 0.128s, 9.37 MB
Maximum runtime on single test case: 0.026s
Final score: 15/15 (3.0/3 points)
"""
N = int(input())
list1 = []


def pro(abc):
    new = abc.split(" ")
    n = int(new[0])
    return new[1] * n


for i in range(N):
    abc = input()
    list1.append(pro(abc))

for i in list1:
    print(i)
