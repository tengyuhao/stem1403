"""
Quiz 10 and homework
"""

# Question 3. A class of student just look a midterm exam on French course.
# Please figure out the average of this class. And how many students got A.

# s is score, and s is student
s_s = [
    ("Marie", 85),
    ("Phoebe", 78),
    ("Sabrina", 96),
    ("Emma", 85),
    ("Amy", 73),
    ("Isabelle", 59),
    ("Clark", 45)
]

# name = ["Marie", "Phoebe", "Sabrina", "Emma", "Amy", "Isabelle", "Clark"]
# score = [85, 78, 96, 85, 73, 59, 45]
# score_total = s_s[0][1] + s_s[1][1] + s_s[2][1] + s_s[3][1] + s_s[4][1] + s_s[5][1] + s_s[6][1]

total = 0
for i in s_s:
    total += i[1]
    # print(total)
# print(total)
average_score = total / len(s_s)

# print(score_total)
print("The average score is {:.2f}".format(average_score))


# how many people get A
number = 0
for score in s_s:
    if score[1] >= 90:
        number = number + 1

print("{} students got an A.".format(number))


"""
3.Python Program to Display the 9X9 multiplication Table
1*1=1
1*2=2   2*2=4
1*3=3   2*3=6   3*3=9
1*4=4   2*4=8   3*4=12  4*4=16
1*5=5   2*5=10  3*5=15  4*5=20  5*5=25
1*6=6   2*6=12  3*6=18  4*6=24  5*6=30  6*6=36
1*7=7   2*7=14  3*7=21  4*7=28  5*7=35  6*7=42  7*7=49
1*8=8   2*8=16  3*8=24  4*8=32  5*8=40  6*8=48  7*8=56  8*8=64
1*9=9   2*9=18  3*9=27  4*9=36  5*9=45  6*9=54  7*9=63  8*9=72  9*9=81
"""

for i1 in range(1, 10):
    for i2 in range(1, i1 + 1):
        print("{} x {} = {}".format(i1, i2, i1 * i2), end="\t")

    print()

