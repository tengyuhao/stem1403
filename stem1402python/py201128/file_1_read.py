"""
file read()

read(size)

cursor

absolute path   \  in windows
relative path   /
"""


# file = open("homework/csvdata.csv")
# file = open("../py201121/csvdata.csv")
file = open("file_1.txt", encoding="utf-8")

# size - integer
# size - char or byte
# size = number of char
content = file.read(6)

print(content)

content = file.read(6)
print(content)

file.close()