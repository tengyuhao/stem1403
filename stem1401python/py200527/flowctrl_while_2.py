"""
simulate do-while loop with python
"""

# while True:
#     print("This is a while loop")
#     if 5 > 3:
#         break


# input a number
# if this number does fall in [1-10]
# re-enter

num = int(input("Enter a number [1-10]: "))

while num < 1 or num > 10:
    num = int(input("Enter a number [1-10]: "))

