"""
open a file
operate
close

file path(location)
file name
file path + file name

When to omit file path?
under the same director or path

file path :
1. absolute path
/Users/kevinteng/PycharmProjects/stem1402b/py201121/file1.txt
2. relative path
file1.txt

"""
# import os
# import os.path
# /Users/kevinteng/PycharmProjects/stem1402b/py201121/file1.txt

print("Start opening file...")
file_path = "../py201114/file_1.py"
print("\t"+file_path)
file = open(file_path)

print("Closing")
file.close()

print("Done")