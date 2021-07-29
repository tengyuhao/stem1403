"""
output
print
string format()
"""

print("This is my book.")

print("This is my bike.")

print("This is my pen.")

# pattern
# string pattern

# "This is my {}"

# {} is the place holder
# string template

print("This is my {}")
# pass a literal
print("This is my {}".format("book"))

# pass a variable
thing = "pen"
print("This is my {}".format(thing))

# pass a variable
template = "This is my {}"
thing = "pen"
print(template.format(thing))


# pass multiple values
thing1 = "pen"
thing2 = "bike"
print("This is my {} and {}.".format(thing1, thing2))


# pass
print("This is my {} and {}.".format(thing2, thing1))

# to specify the order
# argument of the function - format()
# positional argument
print("This is my {1} and {0}.".format(thing1, thing2))
print("This is my {0} and {1}.".format(thing1, thing2))


thing1 = "pen"
thing2 = "bike"
thing3 = "desk"
thing4 = "ipad"
print("This is her {1} , {0} and my {3} in the {2}.".format(thing1, thing2, thing3, thing4))

# name argument
print("This is her {t2} , {t1} and my {t4} in the {t3}.".format(t1=thing1, t2=thing2, t3=thing3, t4=thing4))

# compare print(), print string.format()



