"""
write content  to a file

x mode
"""

try:
    file = open("file12.txt", 'x')

    file.close()
except FileExistsError as fe:
    print(fe)

print("Content has been written")
