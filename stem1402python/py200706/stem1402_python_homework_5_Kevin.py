"""
Fibonacci sequence
"""


def fibonacci(position):
    item = 0
    item_before = 1
    # item_before2 = 0
    for position in range(position):
        item_before2 = item_before
        item_before = item
        item = item_before + item_before2
    return item


print("==== Fibonacci sequence ====")
position = int(input("Write the position of the Fibonacci number: "))

print("At the position {}, the number is {}.".format(position, fibonacci(position)))


for i in range(1, position + 1):
    print(fibonacci(i), end="\t")

print("\n=========== Fin ============")

