"""
N = int(input())

for i in range(N):
  pass

if last letter != this letter:
list.append(letter, num)

else:
num +=1

"""

N = int(input())
num = 0
last_letter = None
list_res = []
num2 = 0
for i in range(N):
    abc = list(input())
    for i in range(len(abc)):
        if last_letter != abc[i]:
            # print("!=")
            res = num+1, last_letter
            list_res.append(res)
            res = None
            num = 0
        elif last_letter == abc[i]:
            num += 1
            # print()
        elif last_letter == False:
            pass
        else:
            pass
        last_letter = abc[i]
        num2 +=1

    res = num + 1, last_letter
    list_res.append(res)
    print(res)
    res = None
    num = 0
    # print(list_res)
    # for i in list_res:
    #     if i == (1, None):
    #         pass
    #     else:
    #         print(f"{i[0]} {i[1]}", end=" ")
print(list_res)
