"""

"""

# user input()
mylist = []
mylist.append(input("Enter a value 1: "))
mylist.append(input("Enter a value 2: "))
mylist.append(input("Enter a value 3: "))
mylist.append(input("Enter a value 4: "))

print(mylist)

#
import sys

print("==== Start ====")
mylist = ['a', '0', '2', '3']

for value in mylist:
    try:
        result = 1 / int(value)
        print(result)
        print()
    except:
        print(sys.exc_info()[0])
        # break
        print()

print("===== end =====")
