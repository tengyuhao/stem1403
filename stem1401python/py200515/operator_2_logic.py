"""
logic operator - and

and, or, not
"""

bool1 = None
bool2 = None

result = bool1 and bool2
print("Switch #1 is {} and Switch #2 is {}, the light is {}."
      .format(bool1, bool2, result))


bool1 = True
bool2 = False

result = bool1 and bool2
print("Switch #1 is {} and Switch #2 is {}, the light is {}."
      .format(bool1, bool2, result))


bool1 = False
bool2 = True

result = bool1 and bool2
print("Switch #1 is {} and Switch #2 is {}, the light is {}."
      .format(bool1, bool2, result))


bool1 = True
bool2 = True

result = bool1 and bool2
print("Switch #1 is {} and Switch #2 is {}, the light is {}."
      .format(bool1, bool2, result))

