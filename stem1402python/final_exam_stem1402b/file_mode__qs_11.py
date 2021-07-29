"""
11. Please compare write() with writelines()
"""


try:
    file = open("csv123.csv")

    content = file.read()

    file.close()


    file = open("file_2a.txt", 'w')

    file.write(content)
    file.close()


    print("Content has been written")

except FileNotFoundError as fnfe:
    print(fnfe)
except IOError as ioe:
    print(ioe)
except Exception as e:
    print(e)

# writelines()
try:
    file = open("file_2b.txt", 'w')

    file.writelines(["hello", "welcome0"])

    file.close()

    print("Content has been written")

except FileNotFoundError as fnfe:
    print(fnfe)
except IOError as ioe:
    print(ioe)
except Exception as e:
    print(e)

