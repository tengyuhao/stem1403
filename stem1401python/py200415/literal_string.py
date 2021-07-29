"""
string literal
"""

# case 1: normal string with ", '
string = "This is python"
string2 = 'This is Python'
print("strings", string)
print("strings2", string2)

# case 2
char = "C"

# case 3
multiline_str = """This is a multiline string with more than one line code. """
print(multiline_str)

multiline_str = """This is a multiline string
     with more than one line code. 
  1234567890 """
print(multiline_str)

multiline_str = '''This is a multiline string
     with more than one line code. 
  1234567890 '''
print(multiline_str)


# case 4: escaped character
print("This is a multiline string. It is powerful")
print("This is a multiline string. \nIt is powerful")

print("Hello \nworld")
# new line  \n
# \ \
# \ '
# \ "
# \n
# \t

print("This is a quote like \" ")
print("This is a quote like \' ")
print("This is a quote like \t is a quote \t is a quote ")

print("abc'xyz”mn\pq\\nabc")  # abc’xyz”mn\pq\nabc

# case 5: unicode
unicode = u"\u00dcnic\u00f6de"

copywrite = "Copyright. \u00a9 ALl right Reserved. "
print(copywrite)

copyright1 = "\u00a9 2019 copyrights"
print(copyright1)

ibmtm = "IBM\u2122 "
print(ibmtm)

# case 6: raw string
raw_str = r"raw \n string"
print(raw_str)


