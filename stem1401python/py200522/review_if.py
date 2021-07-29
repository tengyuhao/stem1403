"""
if structure - decision making
"""

# case 1. if statement
print("program starts.")
condition = 5 < 3
if condition:
    print("This is block of if")

print("end of program.")


# case 2. if-else statement
print("program starts.")
condition = 4 > 2 and 2 < 1
if condition:
    print("This is if block")
else:
    print("This is else block")

print("end of program.")


# case 3. if-elif-else statement
print("program starts.")
condition = True
condition2 = False
if condition:
    print("if block")
elif condition2:
    print("elif block")
else:
    print("else block")
print("end of program.")

# case 3b. if-elif-else statement
print("program starts.")
condition = False
condition2 = True
condition3 = True
condition4 = True

if condition:
    print("if block")
elif condition2:
    print("elif block2")
elif condition3:
    print("elif block3")
elif condition4:
    print("elif block4")
else:
    print("else block")
print("end of program.")

