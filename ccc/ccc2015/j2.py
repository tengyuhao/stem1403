"""
2015 J2
资源： 0.159s, 9.32 MB
最慢一次测试的运行时间 0.024s
最终得分： 15/15 (3.0/3 points)
"""
sentence = input()
sentence = list(sentence)
# print(sentence)
happy = 0
sad = 0
for i in range(len(sentence)):
    if sentence[i] == ":":
        # print()
        emoji = f"{sentence[i+1]} {sentence[i+2]}"
        if emoji == "- )":
            happy += 1
        if emoji == "- (":
            sad += 1


if happy == sad and happy != 0:
    print("unsure")
elif happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
else:
    print("none")
