
"""

资源： 0.204s, 9.24 MB
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
    result = getIndexOfChar(mychar, WORDS)
    index_charL = getIndexOfChar(mychar, WORDS)
    # print(result)
    indexlist = result

    for x in indexlist:
        for y in indexlist:
            if y >= x:
                # print(indexlist[i], indexlist[i2])
                new_str = WORDS[x:y + 1]
                # print(new_str)
                if new_str == new_str[::-1]:
                    long = len(new_str)
                    if long >= max_long:
                        max_long = long

print(max_long)