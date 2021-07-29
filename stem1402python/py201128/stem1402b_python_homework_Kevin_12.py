"""
[Homework]
1. Read an HTML file
    readline() or readlines()
2. Read a CSV file
    readline() or readlines()
3. Read a CSV file of its first half
    readline() or readlines()
"""

file = open("test_html.html", encoding="utf-8")

print("===")
content = file.readline()
print(content)
print("===")
print("===")
content2 = file.readlines()
print(content2)

print("===")

file.close()
"""
result : 
===
<!DOCTYPE html>

===
===
['<html lang="en">\n', '<head>\n', '    <meta charset="UTF-8">\n', '    <title>Title</title>\n', '</head>\n', '<body>\n', 
'    <h1>Hello everybody</h1>\n', '    <h2> test python</h2>\n', '    <p> my homework</p>\n', '\n', '</body>\n', 
'</html>']
===
"""
# Question 2

file = open("business-price-indexes-september-2020-quarter-corrections-to-previously-published-statistics.csv", encoding="utf-8")

print("===")
content = file.readline()
print(content)
print("===")
print("===")
content2 = file.readlines()
print(content2)

print("===")
file.close()
"""
===
"Series reference","Description","Period","Previously published","Revised"

===
===
['"PPIQ.SQU900000","PPI output index - All industries ","2020.06",1183,1184', '"PPIQ.SQU900001","PPI output index - 
All industries excl OOD","2020.06",1180,1181', '"PPIQ.SQUC76745","PPI published output commodity - Transport support services","2020.06",1400,1603',
 '"PPIQ.SQUCC3100","PPI output index level 3 - Wood product manufacturing","2020.06",1169,1170', '"PPIQ.SQUCC3110",
 "PPI output index level 4 - Wood product manufacturing","2020.06",1169,1170', 
 '"PPIQ.SQUFF0000","PPI output index level 1 - Wholesale trade","2020.06",1132,1133',
 '"PPIQ.SQUFF1000","PPI output index level 2 - Wholesale trade","2020.06",1132,1133',
  '"PPIQ.SQUFF1100","PPI output index level 3 - Wholesale trade","2020.06",1132,1133', 
...
===

"""


# Question 3

file = open("business-price-indexes-september-2020-quarter-corrections-to-previously-published-statistics.csv", encoding="utf-8")

print("===")
content = file.readline(40)
print(content)
print("===")
print("===")
content = file.readlines()
n = len(content)
print(n)
n = n/2
n += 1
n = int(n)
print(n)

content2 = file.readlines(1)
print("test", content2)

print("===")
file.close()
"""
===
"
===
===
['Series reference","Description","Period","Previously published","Revised"\n']
==="""


