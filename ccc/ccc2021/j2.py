# set1 = {}
#
# number_of_people = int(input(""))
# for i in range(number_of_people):
#     name = input("")
#     num = int(input())
#     set2 = {name:num}
#     set1.update(set2)
#
#
# result = dict(sorted(set1.items(), key=lambda item: item[1]))
# res2 = list(result.items())
# # print(res2)
# result = list(result.items())
# for i in range(number_of_people-1):
#     if res2[i][1] == res2[i+1][1]:
#         print(result[0][0])
#         import sys
#         sys.exit()
#
# print(result[-1][0])

list1 = []
list2 = []
number_of_people = int(input())
for i in range(number_of_people):
    name = input()
    num = int(input())
    list2.append(name)
    list1.append(num)


# print(list1.index(max(list1)))
n = list1.index(max(list1))
print(list2[n])
