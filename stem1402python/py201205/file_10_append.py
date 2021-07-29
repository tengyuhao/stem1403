"""
write content  to a file

append() -  add content at the tail by default

if the target file does not exist, then create it immediately
"""



file = open("file9.txt", 'a')

content = "File 10, This is the new content I'd like to save. \n"

file.write(content)


file.close()

print("Content has been written")
