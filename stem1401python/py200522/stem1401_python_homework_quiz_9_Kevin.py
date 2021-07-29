"""
Quiz 9 and homework(product)
"""

# Question 1. Please write down all the variations of branching structure
# if
print("=========== Start ===========")
print("test your note is good? if not good, the system will say nothing "
      "(This is for you not to be embarrassed！)")
note = 100
print("~~ For test ~~ You have {} points".format(note))

if note == 100:
    print("Good job, you have scored 100 points")
print("============ End ============")
print()

# if - else
print("=========== Start ===========")
note = 99
print("~~ For test ~~ You have {} points".format(note))

# note = 100
if note == 100:
    print("Good job, you have scored 100 points")
else:
    print("Make persistent efforts, you haven't scored 100 points yet")
print("============ End ============")
print()

# if - elif - else
# 1 or 2 or 3 is number
print("=========== Start ===========")
print("In order to know which exam you are going to do?")
print("For test, please enter the number before 0 to 3 !!!")
exam = input("Please write down the number of exams you must take! (In your Agenda) : ")
exam = int(exam)
list_exam = ["English", "Math", "Python (Computer)"]

if exam == 1:
    print("You have {} exam, this is {}'s exam".format(exam, list_exam[0]))
elif exam == 2:
    print("You have {} exams, this is {} and {}'s exam}".format(exam, list_exam[0], list_exam[1]))
elif exam == 3:
    print("You have {} exams, this is {}, {}, and {}'s exam".format(exam, list_exam[0], list_exam[1], list_exam[2]))
else:
    print("There are only three exams in total to do, and at least one exam to do. \n"
          "So this number is wrong! :(, if you have any question , please send the e-mail to"
          "info@collegeNone.ca")
print("============ End ============")
print()

# nested if
print("=========== Start ===========")
print("Your teacher said, if your 2 exams's average score is below 70 points or you don't do homework, "
      "\nyou will do another work in the school! ")
print("This program wills tell you which work to do! :)")

# hw is mean homework
points = 100
points2 = 100
hw_type = False
# points = 55
# points2 = 20
# type = True

if points + points2 / 2 > 70:
    if hw_type == False:
        print("You will do the fifth unit of the math workbook and English workbook.")
    else:
        print("You can go to your home immediately!")
elif points + points2 / 2 <= 70:
    print("You will do the fifth unit of the math workbook and English workbook.")
elif points + points < 200:
    print("Your notes is wrong, please try again.")
else:
    print("You can go to your home immediately!")
print("============ End ============")
print()

# Programming and answer questions
# Question 2. Write a program to get the min and and max number
# from a given list of 10 numbers
print("=========== Start ===========")
list1 = [99, 100, 66, 777, 5, 666, 5050, 888, 10000]
largest_number = list1[0]
smallest_number = list1[0]

for number in list1:
    if largest_number < number:
        # print("For now, the largest number is {}".format(largest_number))
        # print("For now, the number is {}".format(number))
        largest_number = number
        # print()
        # print("For now, the largest number is {}".format(largest_number))
        # print("For now, the number is {}".format(number))
    # print()
    if smallest_number > number:
        smallest_number = number

print("The largest number is {}".format(largest_number))
print("The smallest number is {}".format(smallest_number))
print("============ End ============")
print()

# homework
# product of 1...20
print("=========== Start ===========")
product = 1     # because  every numbers * 0 = 0
for i in range(1, 21):
    product = product * i

print("My calculator said the product is 2.43290200817664e18")
print("product of 1 to 20 is {}".format(product))
print("============ End ============")

# product of 1...100
print("=========== Start ===========")
product = 1     # because  every numbers * 0 = 0
for i in range(1, 101):
    product = product * i

print("product of 1 to 100 is {}".format(product))
print("============ End ============")
