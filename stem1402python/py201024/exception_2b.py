"""
keyword:    try, expert (exception)
"""

def fa():
    print("fa()")
    try:
        fb()
    except:
        print(sys.exc_info()[0])
        print()


def fb():
    print("fb()")
    fc()

def fc():
    print("fc()")
    # print(a)
    print(1+"str1")



# main program
# call fa()
import sys

print("==== Strat ====")
fa()
print("==== End ====")
