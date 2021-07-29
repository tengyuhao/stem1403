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
2. relative path

"""
# import os
# /Users/kevinteng/PycharmProjects/stem1402b/py201121/file1.txt
print("Start opening file...")
file = open(r"/Users/kevinteng/PycharmProjects/stem1402b/py201121/file1.txt")

print("Closing")
file.close()

print("Done")