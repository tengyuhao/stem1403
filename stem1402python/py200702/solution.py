"""

"""


def foo(numbers):
    max_number = numbers[0]
    for current_number in numbers:
        if max_number < current_number:
            max_number = current_number
    return max_number


mynumbers = [100, 45, 33]
print(f"The max number is {foo(mynumbers)}")
print(f"The max number is {max(mynumbers)}")




