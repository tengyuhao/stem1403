"""
write content  to a file

write()
"""



file = open("file7.txt", 'w')

content = "This is the content I'd like to save."

file.write(content)

file.close()

print("Content has been written")