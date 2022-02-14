"""
CCC 2016 J3

Resources: 0.207s, 9.28 MB
Maximum runtime on single test case: 0.026s
Final score: 15/15 (5.0/5 points)
"""


def getIndexOfChar(char, words):
    index_char = []
    for index, c in enumerate(words):
        if char == c:
            index_char.append(index)
    return index_char


def getIndexPair(indexlist):
    global max_long
    for i in range(len(indexlist)):
        for i2 in range(len(indexlist)):
            # if indexlist.index(indexlist[i2]) >= i:
            if indexlist.index(indexlist[i2]) >= i:
                # print(indexlist[i], indexlist[i2])
                new_str = WORDS[indexlist[i]:indexlist[i2]+1]
                # print(new_str)
                if new_str == new_str[::-1]:
                    long = len(new_str)
                    if long >= max_long:
                        max_long = long

    # return max_long


# main program
max_long = 0
WORDS = input()

for i in WORDS:
    mychar = i
    result = getIndexOfChar(mychar, WORDS)
    index_charL = getIndexOfChar(mychar, WORDS)
    # print(result)
    # max_long = getIndexPair(index_charL)
    getIndexPair(index_charL)


print(max_long)