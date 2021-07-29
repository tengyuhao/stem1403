"""
flow control

loop type 1. for loop

"""

# for-loop print out 100 times of next
print("It is a nice day!")

# syntax
# for var in sequence:
#     body of for

# for i in [0,0,0,0,0,0,0,0,0,0,
#           0,0,0,0,0,0,0,0,0,0,
#           0,0,0,0,0,0,0,0,0,0,
#           0,0,0,0,0,0,0,0,0,0,
#           0,0,0,0,0,0,0,0,0,0,
#           0,0,0,0,0,0,0,0,0,0,
#           0,0,0,0,0,0,0,0,0,0,
#           0,0,0,0,0,0,0,0,0,0,
#           0,0,0,0,0,0,0,0,0,0,
#           0,0,0,0,0,0,0,0,0,0,
#           ]:
#     print("It is a nice day!")


# range()
print(range(10))
print(list(range(10)))


for i in range(1000):
    print("It is a nice day!", i)


print(range(1, 11))
print(list(range(1, 11)))


print(range(1, 11, 2))
print(list(range(1, 11, 2)))



