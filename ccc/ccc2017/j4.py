def check(time):
    global total
    if len(time) == 3:
        d1 = int(time[1]) - int(time[0])
        d2 = int(time[2]) - int(time[1])
        # print(d1, d2)
        if d1 == d2:
            total += 1
            # print(time)
    else:
        d1 = int(time[1]) - int(time[0])
        d2 = int(time[2]) - int(time[1])
        d3 = int(time[3]) - int(time[2])
        if d1 == d2 == d3:
            total +=1
            # print(time)


def convert(timeminutes, hour, minutes):
    if minutes < 10:
        time = f"{hour}0{minutes}"
    elif timeminutes > 720:
        timeminutes -= 720
        time = f"{hour}{minutes}"
        # print(time)
    else:
        time = f"{hour}{minutes}"

    return time
    # print(time)


# main
# time = "1200" + timeinminutes
timeminutes = int(input())
total = 0
sequence = 31    # to calculate

hour = timeminutes // 60
minutes = timeminutes % 60
new_min = 0
new_hour = 12
# print(hour)
if hour == 0:
    hour = 12
while True:
    if new_min == minutes and new_hour == hour:
        break
    new_min += 1
    if new_min == 60:
        new_hour += 1
        new_min = 0
    if new_hour == 13:
        new_hour = 1
    # print(new_hour, new_min)
    # convert(timeminutes, new_hour, new_min)
    check(convert(timeminutes, new_hour, new_min))

print(total)
