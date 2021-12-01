position = ""
list2 = []
while True:
    num = input()
    if num == "99999":
        break
    else:
        list1 = []
        list1 += num
        res = int(list1[0]) + int(list1[1])
        # print(res)
        if res % 2 == 1:
            position = "left"
        elif res % 2 == 0 and res != 0:
            position = "right"
        else:
            position = last_position

        last_position = position
        a = position, f"{list1[2]}{list1[3]}{list1[4]}"
        list2.append(a)


for i in range(len(list2)):
    print(f"{list2[i][0]} {list2[i][1]}")

