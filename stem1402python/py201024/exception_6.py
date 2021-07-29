"""
catching multiple specific exception
"""



print("==== Start ====")
mylist = ['5', 'a', '0', '2', '3']


for value in mylist:
    try:
        result = 1 / int(value)
        print(result)
        print()
    except ValueError:
        print("ValueError")
        print()
    except (TypeError, ZeroDivisionError):
        print("TypeError or ZeroDivisionError")
        print()
    except Exception:
        print("Error")
        print()

print("===== end =====")
