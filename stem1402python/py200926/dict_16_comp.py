"""
dictionary comprehension

1. Write a Python program to generate and print a dictionary that contains a number (between 1 and n)
in the form (x, x*x).
e.g. User inputs 5
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
n = 10
for i in range(1, n+1):
    key = i
    value = key * key
    print(key, value)

# {key: key*key }
# {key: key*key for key in range(1, n+1)}
mydict = {key: key*key for key in range(1, n+1)}

print(mydict)


# ex 1.
# version 1
n = 10
mydict = {key: key+key+1 for key in range(1, n+1)}
print(mydict)
# {1: 3, 2: 5, 3: 7, 4: 9, 5: 11, 6: 13, 7: 15, 8: 17, 9: 19, 10: 21}


# version 2
def getdict(n):
    mydict = {key: key + key + 1 for key in range(1, n + 1)}
    return mydict


print(getdict(11))

# automated
print("========= Automated test ==========")
testdata = [2, 5, 10, 18, 22]

for i in testdata:

    print(getdict(i))
