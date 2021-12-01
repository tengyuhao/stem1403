"""
CCC 2021 Junior
J4. Arranging books

Resources: 0.459s, 10.08 MB
Maximum runtime on single test case: 0.113s
Final score: 15/15 (7.0/7 points)
"""

books = input()

NumL = 0
NumM = 0

for book in books:
    if book == 'L':
        NumL += 1
    elif book == 'M':
        NumM += 1
    else:
        pass

sectionL = books[:NumL]
sectionM = books[NumL:NumL + NumM]

def getNonChar(mystr, char):
    n = 0
    for c in mystr:
        if char != c:
            n += 1
    return n


def getChar(mystr, char):
    n = 0
    for c in mystr:
        if char == c:
            n += 1
    return n


non1 = getNonChar(sectionL, 'L')
non2 = getNonChar(sectionM, 'M')

n1 = getChar(sectionL, 'M')
n2 = getChar(sectionM, 'L')

print(non1 + non2 - min(n1, n2))