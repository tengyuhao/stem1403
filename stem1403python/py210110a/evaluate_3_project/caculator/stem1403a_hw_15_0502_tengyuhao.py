"""
Study others' code
"""


# reference : project of Zeyue Li
def execute_button(button):
    global operation
    if button != "C" and button != "DEL":
        operation += button
    elif button == "C":
        operation = ""
    else:
        operation = operation[:-1]
    # display_label["text"] = f"{operation}\n{result}



"""
Use if-elif-else statement to do the logic of the clear, delete, and show in the display label.
buttons = ["C", "7", "4", "1", "DEL", "8", "5", "2", "%", "9", "6", "3", "/", "*", "-", "+"]
Because just 'C' and 'DEL' is not work with eval statement and + - * / is work with eval statement
"""

MAXROW = 5
"""Also, it's a good idea to create a variable for the rows and columns."""

# reference : project of KEvin iu

# if expression[-1:].isnumeric and expression != "":
#     expression = expression + "+"
# display_Label.config(text=expression)

""" use isnumeric to check if you repeated or not. After with one function to use it. """






