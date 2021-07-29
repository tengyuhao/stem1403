"""
write content  to a file

write() - overwrite
if the target file does not exist, then create is immediately

Idddddddddddddddddd
"""



file = open("file9.txt", 'w')

content = "File 9, This is the new content I'd like to save. \n"

file.write(content)

# file.seek(0)
file.seek(10)

file.write(content)

file.close()

print("Content has been written")
