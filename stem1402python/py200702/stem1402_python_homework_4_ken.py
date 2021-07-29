"""
For July 6th, 2020.
stem1402_python_homework_5_ken
Ken
"""

# Fibonacci sequence
# Position starts with 0
def fibonacci_finder(position):
    """
    A fibonacci number at a certain is the sum of the number behind it and the number behind this number that is behind it
        (x8 = x7 + x6)

    item = the number at the latest position
    itembefore = the number behind item
    itembefore2nd = the number behind itembefore

    A for loop is used to run the block of
        itembefore2nd = itembefore
        itembefore = item
        item = itembefore + itembefore2nd
    a certain number of times.

    At the start, item is equal to 0 so that if the position entered is 0, the number will be 0.
    itembefore starts off as 1 since in the block, itembefore (= to 1) and itembefore2nd (= to 0) make 1.

    If itembefore was equal to 0, an endless loop of 0 + 0 would be made since the first line is itembefore2nd = itembefore

    :param position: position in the sequence
    :return: number at the position in the sequence
    """
    item = 0
    itembefore = 1
    itembefore2nd = 0
    for position in range(position):
        itembefore2nd = itembefore
        itembefore = item
        item = itembefore + itembefore2nd
    return item


print("""---Fibonacci number generator---""")

position = int(input("Write the position of the Fibonacci number: "))

print("At position {}, the number is {}.".format(position, fibonacci_finder(position)))

for i in range(1, 101):
    print(fibonacci_finder(i), end="\t")

# test
