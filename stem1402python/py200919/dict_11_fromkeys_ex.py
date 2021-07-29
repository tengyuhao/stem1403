"""

"""
str1 = "python is a good language"

keys = set(str1)
print(keys)

charcount = {}
# charcount = charcount.fromkeys(keys)
charcount = charcount.fromkeys(keys, 0)

print(charcount)

for char in str1:
    charcount[char] += 1

print(char)
