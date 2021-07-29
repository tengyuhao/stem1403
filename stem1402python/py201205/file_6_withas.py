"""
with ... as
open and operate on a file
recommended
"""

with open("homework/myweb.html") as file:
    content = file.read()

print(content)


print("--------------")

file = open("homework/myweb.html")
try:
    content = file.read()
    print(content)
finally:
    file.close()