"""
filemode

r
w
a
x

t,b

+

write a program to have a trial with r+
"""
f1 = open("filemode_1.txt", 'w')
f1.close()

file = open("filemode_1.txt", 'r+')
content = file.read()
print(content)

comment = "asdfjamdsndfnsajkf"
file.write(comment)

file.close()
print("The first comment is has been write")





