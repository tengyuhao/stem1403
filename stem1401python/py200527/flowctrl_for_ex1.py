"""

"""

# v1
for i in range(1, 13):
    product = 12 * i
    print("12 * {:2} = {:3}".format(i, product))

# v2 - kevin
number = input("Please enter one number : ")
number = int(number)

for i in range(1, number + 1):
    product = number * i
    print("{} X {:2} = {:3}".format(number, i, product))
