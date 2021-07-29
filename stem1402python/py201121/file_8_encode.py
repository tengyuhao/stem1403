"""
file mode

encoding:
utf-8
ascii
cp1252
"""
# import os
# import os.path
try:
    print("Start opening file...")
    filepath = "../py201121/file8.txt"
    print("\t"+filepath)
    file = open(filepath, 'rt', encoding="utf-8")
    content = file.read()
    print(content)
    print("Closing...")
    file.close()
except FileNotFoundError as fe:
    print(fe)
except IOError as ioe:
    print(ioe)
except Exception as e:
    print(e)
print("Done.")