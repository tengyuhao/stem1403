"""
2015 J3
资源： 0.123s, 9.33 MB
最慢一次测试的运行时间 0.027s
最终得分： 20/20 (5.0/5 points)
"""
string_before = input()
string_before = list(string_before)

VOYELLES = [97, 101, 105, 111, 117]
res = ""
for i in string_before:
    i_num = ord(i)
    if i_num in VOYELLES:
        res += i
    else:
        res += i
        min_num = 0
        list1 = []
        if i_num < 100:
            res += 'a'
        else:
            for i2 in range(len(VOYELLES)):
                if i2 == len(VOYELLES)-1:
                    pass
                else:
                    num1 = i_num - VOYELLES[i2]
                    num2 = i_num - VOYELLES[i2+1]
                    if num1 < 0:
                        num1 = abs(num1)
                    if num2 < 0:
                        num2 = abs(num2)

                    num3 = min(num1, num2)
                    list1.append(num3)
            ind = list1.index(min(list1))
            res += chr(VOYELLES[ind+1])
        if i == 'z':
            res += 'z'
        else:
            if i_num + 1 in VOYELLES:
                res += chr(i_num+2)
            else:
                res += chr(i_num+1)

print(res)
