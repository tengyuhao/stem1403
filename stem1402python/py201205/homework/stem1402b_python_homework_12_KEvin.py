"""
1. Read an HTML file, and copy all content into a new file
2. Read a CSV file, and copy all content into a new file
3. Read a CSV file, and copy its first half lines into a new file
"""

# Question 1.
try:
    file = open("myweb.html")

    content = file.read()

    file.close()


    file = open("myweb.txt", 'w')

    file.write(content)
    file.close()


    print("Content has been written")
except FileNotFoundError as fnfe:
    print(fnfe)
except IOError as ioe:
    print(ioe)
except Exception as e:
    print(e)
# Question 2.

file = open("business-price-indexes-september-2020-quarter-corrections-to-previously-published-statistics.csv")

content = file.read()

file.close()


file = open("business-price-indexes-september-2020-quarter-corrections-to-previously-published-statistics.txt", 'w')

file.write(content)
file.close()


print("Content has been written")


# Question 3.
file = open("business-price-indexes-september-2020-quarter-corrections-to-previously-published-statistics.csv")

num = len(file.readlines())
if num % 2 == 0:
    line = int(num / 2)
    print(line)
elif num % 2 == 1:
    line = int(num + 1)
    line = int(line / 2)
    print(line)
file.seek(0)


file2 = open("csvmodified.txt", 'w')
file2.close()

for i in range(line):
    content = file.readline()

    file3 = open("csvmodified.txt", 'a')

    file3.write(content)
    file3.close()

file.close()
print("Content has been written")
