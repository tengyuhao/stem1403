"""
exam final
"""
# Please write down the syntax for each one of
# them including variations.

# if statement
condition = True
if condition == True:
    print("The condition is {}".format(condition))

# if-else statement
condition = False
if condition == True:
    print("The condition is {}".format(condition))
else:
    print("The condition is False")

# if-elif-else statement
note = 90
if note == 100:
    print("Excellent, you scored 100 points for your exam.")
elif note >= 90:
    print("Good job, you got an A!")
elif note >= 80:
    print("Keep going, you got a B!")
else:
    print("Make persistent efforts, you score is below 80.")

# for loop
for i in range(1, 11):
    print(i)

# while loop
num = int(input("Enter a number [1-10]: "))
while num < 1 or num > 10:
    num = int(input("Enter a number [1-10]: "))

# import one another file in the one python file
import exam_final.import_constant_1 as const
radius = 100
area = const.PI * radius * radius
print(area)
