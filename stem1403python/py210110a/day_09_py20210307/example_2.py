#   Canadian Computing Competition
#
#    Example program to demonstrate input and output and time limit.
#
#    Programming Language:  Python 3.x
#
#    Specification:
#
#       Write a program that reads several positive integers, one per
#       line.  For each integer n, output the number of orderings
#       possible for a set of n distinct values.  n will not exceed 11.
#       The last line of input is indicated by 0.
#
#    Sample Input:
#
#       1
#       9
#       0
#
#    Output for Sample Input:
#
#       1
#       362880
#
#    Implementation:
#
#       The answer is n! (n factorial) which is easily computed in n steps.
#       But this program does it the hard way.  It uses a recursive function
#       to enumerate and count all the possible orderings.
#
#    How to run the program:
#
#       The program reads from "standard input" and writes to "standard output."
#       Specifically, you can  this program with input by typing at the
#       DOS command prompt (yes, you will need a Command Prompt window)
#       in the correct directory (where you created the test.py2 file):
#                 python test2.py < input.txt
#       where input.txt contains the test data.
#
#    Run-time:
#
#       Please time the execution time of this program on your computer,
#       using the sample input.  This time is the maximum that should be
#       allowed for any CCC program.  Note that this solution will work
#       only up to problems of size 9 in the required time limit
#
res = 0
def factorial(n):
  for i in range(0, n):
    result = n * i

    res = res + result
  return res


num = input("Please input one number : ")
num = int(num)
print(factorial(num))