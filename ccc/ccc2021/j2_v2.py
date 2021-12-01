
list1 = []
list2 = []
number_of_people = int(input(""))
for i in range(number_of_people):
    name = input("")
    num = int(input())
    list2.append(name)
    list1.append(num)


# print(list1.index(max(list1)))
n = list1.index(max(list1))
print(list2[n])

