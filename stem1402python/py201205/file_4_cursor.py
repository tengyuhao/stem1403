"""
file cursor

seek()

tell()

"""

file = open("homework/myweb.html")

content = file.read()

print(content)
print("=================")
# read from start
file.seek(0)
content2 = file.read()
print(content2)
print("=================")

file.close()

print("\n\n")

#


file2 = open("homework/myweb.html")

content = file2.read(4)

print(content)
print("=================", end="\n")
# read from start
file2.seek(9)
content2 = file2.read(4)
print(content2)
print("=================")

file.close()
