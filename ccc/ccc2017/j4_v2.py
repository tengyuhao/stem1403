"""
2017 J4
资源： 0.443s, 9.52 MB
最慢一次测试的运行时间 0.027s
最终得分： 15/15 (5.0/5 points)
"""


def check(time):
    global total
    abc = 0
    for i in range(len(time)-1):

        diff = int(time[i+1]) - int(time[i])
        # print(diff)
        if i == 0:
            last_diff = diff

        if diff == last_diff:
            abc += 1
            if abc == len(time)-1:
                total += 1

def convert(hour, minutes):
    global total
    if minutes < 10:
        time = f"{hour}0{minutes}"
    else:
        time = f"{hour}{minutes}"

    return time
    # print(time)


# main
timeminutes = int(input())
total = 0
sequence = 31    # to calculate
if timeminutes >= 720:
    n = timeminutes // 720
    timeminutes -= 720 * n
    total += 31 * n

hour = timeminutes // 60
minutes = timeminutes % 60
new_min = 0
new_hour = 12
if hour == 0:
    hour = 12
# print(hour, minutes)

while True:
    if new_min == minutes and new_hour == hour:
        break
    else:
        new_min += 1
        if new_min == 60:
            new_hour += 1
            new_min = 0
        if new_hour == 13:
            new_hour = 1
    # print(new_hour, new_min)
    # convert(timeminutes, new_hour, new_min)
    check(convert(new_hour, new_min))

print(total)
