"""
file
readlines()

readlines() v.s. readlime()

readline - read file line by line, suport to read large file
readlines - read all content of a file into a list
            access .......

read() - read all content of a file
read(size) - read a certain number of a chars, supporting big file
"""



# file = open("homework/csvdata.csv")
# file = open("../py201121/csvdata.csv")
file = open("file_1.txt", encoding="utf-8")

# size - integer
# size - char or byte
# size = number of char
print("===")
content = file.readlines()

print(content, type(content))

for line in content:
    print(line, end="")
print("===")

# readline #2
lineno = 1
res = content[lineno]
print(res)

file.close()
