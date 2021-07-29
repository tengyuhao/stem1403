"""
catching specific exception
and print out error message

keyword: as
"""


print("==== Start ====")
mylist = ['5', 'a', '0', '2', '3']


for value in mylist:
    try:
        result = 1 / int(value)
        print(result)
        print()
    except ValueError as ve:
        print(ve)
        print()
    except ZeroDivisionError as zde:
        print(zde)
        print()
    except TypeError as te:
        print(te)
        print()
    except Exception as ex:
        print("Error")
        print(ex)
        print()

print("===== end =====")
