"""
lambda and filter()
"""

# keep even numbers
# drop odd numbers
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = []
for i in my_list:
    if i % 2 == 0:
        result.append(i)

print(result)

# filter() + lambda
res = filter(lambda x: x % 2 == 0, my_list)

print(res, type(res))

# list()
result = list(res)
print(result)



