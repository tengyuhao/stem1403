"""
Exam final
Part 2. Programming (50’)
"""

# 1. Writing a Python program to remove punctuations from a string (20’)
# Description:
# You are asked to write a program to implement the program as described in the title.
# Hints:
#    User's input is a must.
#    The valid punctuation characters are as follows which can be used directly in your code.
#    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#    The processed result of the string should be printed out.
# punctuations = ["!", "(", ")", "-", "[]", "{}", ";", ":", "'", "\\", ",", "<>", ".", "/", "?",
#                 "@", "#", "$", "%", "^", "&", "*", "_", "~"]

print("====================== Start ======================")
# User's input is a must.
sentence = input("Please input something, and the program will remove the punctuations automatic: ")

#  The valid punctuation characters are as follows which can be used directly in your code.
punctuations = ''' !()-[]{};:'"\,<>./?@#$%^&*_~ '''

for sentence in sentence:
    if sentence not in punctuations:
        print(sentence, end="")

print("\n======================= End =======================")

# 2. Counting the number of each character occurring in a given string (20’)
# Description:
# You are asked to write your idea or flowchart to describe how to resolve it.
# Second, write your program to implement it.
# Hints:
#   Data type of Dictionary is recommended to use
#   User input is a must
#   Proper output is a must.

print("====================== Start ======================")
input1 = list(input("Please enter one sentence, and the program will counting the number of each character: "))
dict1 = {
}

for i in input1:
    # print(i)
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] = dict1[i] + 1
    # print(i, dict1[i])
print("The count of character occurring in a given string is: {}".format(dict1))

print("======================= End =======================")

