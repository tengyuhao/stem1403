"""
test if a year is a leap year
"""

print("========== Start ==========")
print("Test if a year is a leap year!!!")

# input the year
year = input("Please input one year: ")

# perform checking
year = int(year)
# print(type(year))
# print(year % 4)

# output the result
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This year is a leap year!")
        else:
            print("This year is not a leap year!")
    else:
        print("This year is a leap year!")

elif year == 0:
    print("This is an invalid year！")

else:
    print("This year is not a leap year!")

print("=========== End ===========")



