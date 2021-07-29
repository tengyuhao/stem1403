"""
decision making - keyword: if
"""

"""
syntax
if condition:
    body of if (code of block)

"""

# example 1 - if statement
# if it is sunny, we would go out for shopping

is_sunny = False
# is_sunny = True

print("==== Start ====")
if is_sunny:
    print("we would go out for shopping!")

print("===== End =====")

print()


# example 2 - if-else statement
print("==== Start ====")
if is_sunny:
    print("we would go out for shopping!")
else:
    print("we would stat at home playing game!")

print("===== End =====")


# example 3 - if-elif-else statement
print()
print("==== Start ====")
score = 100
print("Your scorr is {}".format(score))

if score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
else:
    print("You got a C")
print("===== End =====")

# test for 3 times or 5 times


# example 3 - if-elif-else statement
print()
print("==== Start ====")
score = 100
print("Your scorr is {}".format(score))

if score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
elif score >= 60:
    print("You got a C")
else:
    print("You got a D")

print("===== End =====")


# nested if statement
list1 = [1, 2, 3]
nested_list = ['a', 'b']
# list1 = [1, ['a', 'b'], 3]

list1[1] = nested_list
print(list1)

# nested if statement
score = 100
if score >= 90:
    if score == 100:
        print("TA, helping others")
    else:
        print("Do nothing")
else:
    print("Please write your homework.")
