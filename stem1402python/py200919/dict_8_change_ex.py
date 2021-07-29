"""

"""
# dict_1 = {}
# sentence = "Python is a good language"
# for i in sentence:
#     print(sentence)
#     dict_1[sentence] = []


"""
idea:
determine using data type for dictionary
key : value
char : count

2. initial
char : 0

3. core logic
if key not exist (occurs for the 1st time), adding
else update by increasing  1 to the value
iteration is needed
for-loop
"""


str1 = "python is a good language"

charcount = {}

for char in str1:
    print(char)
    if  char not in charcount:
        charcount[char] = 1
    else:
        charcount[char] += 1

print(charcount)