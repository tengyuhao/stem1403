"""资源： 0.304s, 9.24 MB
最慢一次测试的运行时间 0.026s
最终得分： 15/15 (3.0/3 points)
2018 J2
"""
N = input()

before = list(input())
after = input()
listB = []
listA = []
num =0
for i, element in enumerate(before):
    res = i, element
    listB.append(res)
for i, element in enumerate(after):
    res = i, element
    listA.append(res)
for i in range(len(listB)):
    if listB[i][1] == listA[i][1]:
        if listB[i][1] == "C" and listA[i][1] == "C":
            num +=1

print(num)
# print(listB, listA)