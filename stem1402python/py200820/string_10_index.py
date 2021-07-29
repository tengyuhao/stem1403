"""
index()

The index() method returns the index of a substring inside the string (if found).
If the substring is not found, it raises an exception.
"""

# Example 1
sentence = 'Python programming is fun'

result = sentence.index('let it')
print("Substring 'is fum':", result)

# result = sentence.index('Java')
# print("Substring 'Java':", result)


# Example 2
sentence = 'Python programming is fun.'
print(sentence.index('ing', 10))

print(sentence.index('g is', 10, -4))
# print(sentence.index('fun', 7, 18))
