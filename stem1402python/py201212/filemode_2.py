"""
writelines()

readlines()
"""
try:
    file = open("filemode_2.txt", 'a')

    content_list = ["See you later!", "Good buy", "See you tomorrow!"]
    file.writelines(content_list)

    content_list = ['\n', "See you later!\n", "Good buy\n", "See you tomorrow!"]
    file.writelines(content_list)

    file.close()

    file = open("filemode_2.txt")

    content = file.readlines()
    for line in content:
        print(line)

    file.close()

except Exception as e:
    print(e)