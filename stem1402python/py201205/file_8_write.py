"""
write content  to a file

write() - overwrite
if the target file does not exist, then create is immediately
"""



file = open("file7.txt", 'w')

content = "File 8, This is the new content I'd like to save. \n"

file.write(content)
file.write(content)

file.close()

print("Content has been written")
