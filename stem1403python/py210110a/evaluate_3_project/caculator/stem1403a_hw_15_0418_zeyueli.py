"""
[Homework]
Date: 2021-04-18

Description:
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


def execute_button(button):
    global operation
    if button != "C" and button != "DEL":
        operation += button
    elif button == "C":
        operation = ""
    else:
        operation = operation[:-1]
    display_label["text"] = f"{operation}\n{result}"

def calculate():
    global result
    global operation
    try:
        result = eval(operation)
        operation += "="
        display_label["text"] = f"{operation}\n{result}"
        operation = str(result)
    except Exception as e:
        result = "An error has occurred during the calculation"
        display_label["text"] = f"{result}"
    result = ""


root = Tk()
root.title("Python GUI - Project - Calculator")

operation = ""
result = ""

if result == "":
    display_label = Label(root, text=f"{operation}", relief="raised", width=100, height=2, anchor=E)
else:
    display_label = Label(root, text=f"{operation}\n{result}", relief="raised", width=100, height=2, anchor=E)
display_label.grid(row=0, columnspan=4, sticky=S)

MAXROW = 5

r = 1
c = 0

buttons = ["C", "7", "4", "1", "DEL", "8", "5", "2", "%", "9", "6", "3", "/", "*", "-", "+"]

for button in buttons:
    button1 = Button(root, text=button, font=(None, 10), relief="raised", command=lambda a=button: execute_button(a))
    if button == "C":
        button1["fg"] = "blue"
    button1.grid(row=r, column=c, sticky=E+W)
    r += 1

    if r >= MAXROW:
        c += 1
        r = 1

zero_button = Button(root, text="0", font=(None, 10), relief="raised", command=lambda: execute_button("0"))
zero_button.grid(row=6, columnspan=2, sticky=E+W)

dot_button = Button(root, text=".", font=(None, 10), relief="raised", command=lambda: execute_button("."))
dot_button.grid(row=6, column=2, sticky=E+W)

enter_button = Button(root, text="=", bg="yellow", font=(None, 10), relief="raised", command=calculate)
enter_button.grid(row=6, column=3, sticky=E+W)

root.mainloop()
