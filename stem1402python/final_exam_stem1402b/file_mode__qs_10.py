"""
10. When to use 'append' mode and when to use ' write' mode?
For a ' Log' document which has been already created and has some data records in it,
what file mode is suitable for adding new records to the document? Why?
"""

file = open('file_1.txt', 'a')
content = "hahahha1\n"

file.write(content)


file.close()
print("The docs has been closed.")


"""
Mode append :
The mode append can creat an document if this document is not exist.
And it can write something, and follow the sentence.
"""

"""
Mode write :
The mode append can creat an document if this document is not exist.
And it can replace r=the text if it has something already.
"""