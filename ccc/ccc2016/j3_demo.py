"""
2016 J3
资源： 0.206s, 9.26 MB
最慢一次测试的运行时间 0.026s
最终得分： 15/15 (5.0/5 points)
"""

def getIndexOfChar(char, words):
    index_char = []
    for index, c in enumerate(words):
        # print(index, c)
        if char == c:
            index_char.append(index)
    return index_char


# main program
max_long = 0
WORDS = input()

for i in WORDS:
    mychar = i
    index_charL = getIndexOfChar(mychar, WORDS)

    # print(result)
    for i in range(len(index_charL)):
        for i2 in range(len(index_charL)):
            if index_charL.index(index_charL[i2]) >= i:
                # print(indexlist[i], indexlist[i2])
                new_str = WORDS[index_charL[i]:index_charL[i2] + 1]
                # print(new_str)
                if new_str == new_str[::-1]:
                    long = len(new_str)
                    if long >= max_long:
                        max_long = long

print(max_long)
