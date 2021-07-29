"""
write content  to a file

x mode
"""

try:
    file = open("file13.txt", 'x')
    content = "Test file writing\n"
    file.write(content)
    file.close()

    file = open("file13.txt")
    content = file.read()
    print(content)
    file.close()

    print("file has been create")

except FileExistsError as fe:
    print(fe)

print("Content has been written")
