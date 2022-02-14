"""
2016 J4
资源： 0.326s, 9.48 MB
最慢一次测试的运行时间 0.027s
最终得分： 15/15 (5.0/5 points)
"""


def check(hour):
    global condition
    if hour >= 7 and hour < 10:
        # print("x")
        # print(hour)
        condition = True
    elif hour >= 15 and hour < 19:
        condition = True
    else:
        condition = False

# main program
time_init = input()
hour, minute = time_init.split(":")
hour = int(hour)

condition = None
minute = int(minute)
number_count = 0
while True:
    check(hour)
    if condition == False:
        number_count += 2
    if condition == True:
        number_count += 1
    minute += 10
    if minute == 60:
        hour += 1
        minute = 0

    if number_count >= 24:
        break
    # print(hour, minute)

if hour >= 24:
    hour = hour % 24

if minute < 10:
    # minute = str(minute)
    minute = f"0{minute}"

if hour < 10:
    print(f"0{hour}:{minute}")
else:
    # print()
    print(f"{hour}:{minute}")
# print(hour, minute)
