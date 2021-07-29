"""
file mode
mode letter(s) indicates the operation on files
mode code:
Group 1.
r       open file for reading
w       open file for writing
a       open file for appending
x       open file for creating
Group 2.
t       open a text file
b       open a binary file
Group 3.
+       plus
r+
w+
Combination
rt      read, text file
wt      write,text file
rb
wb
...
r+b
r+t
Default
rt  => r
rt  => default
"""

# import os
# import os.path
try:
    print("Start opening file...")
    filepath = "../day10_201114/review1.py"
    print("\t"+filepath)
    file = open(filepath, 'rt')
    print("Closing...")
    file.close()
except FileNotFoundError as fe:
    print(fe)
except IOError as ioe:
    print(ioe)
except Exception as e:
    print(e)
print("Done.")