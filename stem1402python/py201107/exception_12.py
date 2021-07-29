"""
try structure

finally

try:
    pass
except:
    pass
except:
    pass
else:
    pass
finally:
    pass
"""

try:
    print("Start try-exception program")
    print("run #1")
    print("run #2")
    print("run #3")
    raise ValueError("Raise a value error")
    print()
except ValueError as ve:
    print(ve)
    print()
except Exception as e:
    print("Error")
    print(e)

else:
    print("No Error")
    print()
finally:
    print("finally")
    print("release recourse")

