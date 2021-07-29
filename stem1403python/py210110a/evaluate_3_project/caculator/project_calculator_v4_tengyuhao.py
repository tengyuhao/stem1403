"""
Project Calculator
    Create a window
    Create 10 Button objects for digit 0 - 9
    Create 7 Button objects for operators (+, -, *, /, %, ., =)
    where % stands for modulus operator rather than percentage sign
    where = stands for performing calculation
    Create a "Clear all" Button with the caption of C
    Create a "Backspace" Button with the caption of DEL
    Create a display Label to show expression (or equation) at the first line
    and to show result at the second line.
"""

from tkinter import *


def clear():
    global expression
    displayL.config(text=" " + '\n')
    expression = ""


def delete():
    global expression
    expression = expression[:-1]
    displayL.config(text=expression + '\n')


def arithmetic(operator):
    global expression
    expression += operator
    displayL.config(text=expression + '\n')


def digit(num):
    global expression
    expression += num
    # print(expression)
    displayL.config(text=expression + '\n')


def equal_f():
    try:
        global expression
        answer = expression + '=\n' + str(eval(expression))
        displayL.config(text=answer)

    except Exception:
        answer_error = expression + '=\n' + "ERROR"
        displayL.config(text=answer_error)


# main program
expression = ""
root = Tk()
root.title("Calculator")
root.geometry("840x320")

displayL = Label(height=4, width=38, font=("SF Pro Display", 15, "bold"), relief='raised', anchor=E)
root.update()
displayL.grid(columnspan=4, sticky=E)


Button(root, text="C", command=clear, width=10, height=2).grid(pady=5, row=3, column=0)
Button(root, text="DEL", width=10, height=2, command=delete).grid(pady=5, row=3, column=1)
Button(root, text="%", width=10, height=2, command=lambda operator="%": arithmetic(operator)).grid(pady=5, row=3,
                                                                                                   column=2)
Button(root, text="\u00f7", width=10, height=2, command=lambda operator="/": arithmetic(operator)).grid(pady=5, row=3,
                                                                                                        column=3)
Button(root, text="\u00d7", width=10, height=2, command=lambda operator="*": arithmetic(operator)).grid(pady=5, row=4,
                                                                                                        column=3)
Button(root, text="-", width=10, height=2, command=lambda operator="-": arithmetic(operator)).grid(pady=5, row=5,
                                                                                                   column=3)
Button(root, text="+", width=10, height=2, command=lambda operator="+": arithmetic(operator)).grid(pady=5, row=6, column=3)
Button(root, text="=", width=10, height=2, command=equal_f).grid(pady=5, row=7, column=3)
Button(root, text=".", width=10, height=2, command=lambda operator=".": arithmetic(operator)).grid(pady=5, row=7,
                                                                                                   column=2)


digit_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# r = row, c = column
r = 6
c = 0

for i in digit_list:
    btn = Button(text=i, command=lambda num=i: digit(num), width=10, height=2)
    btn.grid(row=r, column=c)
    if c == 2:
        r = r - 1
        c = 0
    else:
        c = c + 1

btn_zero = Button(root, text="0", width=10, height=2, command=lambda num="0": digit(num))
btn_zero.grid(row=7, column=0, columnspan=2, sticky='we')

root.mainloop()

