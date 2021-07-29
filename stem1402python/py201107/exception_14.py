"""
user-defined exception
case 1. 100
case 2. 1
case 3. 0
case 4. 101
"""

try:
    print("Enter a number between 1 and 100: ", end="")
    num = int(input())

    if num < 1:
        raise ValueError("Number should not be less than 1")

    if num > 100:
        raise ValueError("Number should not be greater than 100")

except ValueError as ve:
    print("ValueError")
    print(ve)
except Exception as e:
    print(e)

finally:
    print("done.")
