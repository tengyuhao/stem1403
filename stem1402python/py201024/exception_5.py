"""
catching specific exception
one try block
multiple exception blocks

"""



print("==== Start ====")
mylist = ['5','a', '0', '2', '3']


for value in mylist:
    try:
        result = 1 / int(value)
        print(result)
        print()
    except ValueError:
        print("ValueError")
        print()
    except ZeroDivisionError:
        print("ZeroDivisionError")
        print()
    except Exception:
        print("Error")
        print()

print("===== end =====")
