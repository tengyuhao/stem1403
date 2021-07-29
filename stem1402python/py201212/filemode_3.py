"""
read specific line(s) #

function signature
"""

def gertline(start_no, end_no):
    pass
def getline(line_no):
    if line_no < 1:
        return "No such line"
    # line_no = 2
    with open("filemode_3.txt") as file:
        data = file.readlines()
        if line_no > line_no:

            return "No such line"
        content = data[line_no-1]
        return content

#  main program
try:
    lineno = int(input("Please enter a line:"))
    print(getline(lineno), end="")

except ValueError as e:
    print(e)
print(getline(1), end="")
print(getline(2), end="")
print(getline(3), end="")
print(getline(4), end="")
print(getline(5), end="")