"""
keyword:    try, expert (exception)
"""


def fa():
    print("fa()")
    fb()


def fb():
    print("fb()")
    fc()


def fc():
    print("fc()")
    # print(a)
    try:
        print(1 + "str1")
    except:
        print(sys.exc_info()[0])
        print()

# main program
# call fa()
import sys

print("==== Strat ====")
fa()
print("==== End ====")
