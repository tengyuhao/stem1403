"""
file
readline()

checksum
"""


# file = open("homework/csvdata.csv")
# file = open("../py201121/csvdata.csv")
file = open("file_1.txt", encoding="utf-8")

# size - integer
# size - char or byte
# size = number of char
print("===")
content = file.readline()

print(content, end="")

content = file.readline(6)
print(content)

content = file.readline(-1)
print(content)

content = file.readline(500)
print(content)

content = file.readline(29)
print(content)
print("===")
file.close()