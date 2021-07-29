"""
[Homework]
Date: 2021-04-10
Design and write program for a login form
Requirements:
A GUI interface
Preset the username is 'admin' and the password is '123456'
User may input username
User may input password, and the password should show mask char ('*') instead
If the user's input matches the presetting, then the program shows a text message (info) box with the words 'login successfully!'
otherwise, the program shows a text message (error) box with the words 'wrong username or password!'
Due date: by the end of next Friday
"""
from tkinter import *

root = Tk()
root.title("Python GUI - calculator")

row = 2
digits = ['7', '4', '1', '8', '5', '2', '9', '6', '3']
col = 0
answer = '0'


# calculator functions
def clear():
    global answer
    answer = '0'
    calculator_screen.config(text=answer)


def backspace():
    global answer
    calculator_screen.config(text=answer[:-1])
    answer = answer[:-1]
    if len(answer) == 0:
        answer = '0'


def add():
    global answer
    answer = answer + '+'
    calculator_screen.config(text=answer)


def sub():
    global answer
    answer = answer + '-'
    calculator_screen.config(text=answer)


def multiply():
    global answer
    answer = answer + '*'
    calculator_screen.config(text=answer)


def divise():
    global answer
    answer = answer + '/'
    calculator_screen.config(text=answer)


def modulus():
    global answer
    answer = answer + '%'
    calculator_screen.config(text=answer)


def comma():
    global answer
    answer = answer + '.'
    calculator_screen.config(text=answer)


def number(num):
    global answer
    if answer == '0' and len(answer) == 1:
        answer = num
        calculator_screen.config(text=num)
    else:
        answer = str(answer) + num
        calculator_screen.config(text=answer)
        root.update()


def zero():
    global answer
    if answer == '0' and len(answer) == 1:
        answer = '0'
    else:
        answer = answer + '0'
    calculator_screen.config(text=answer)


def equal():
    global answer
    answer_expression = answer + '\n' + str(eval(answer))
    calculator_screen.config(text=answer_expression)


# calculator display screen
calculator_screen = Label(text=answer, relief='raised', height=2, width=34, anchor=SE, padx=3, font='Times 24')
calculator_screen.grid(row=0, columnspan=4)

# calculator buttons
clear_button = Button(root, text='C', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12', fg='blue',
                      command=clear)
clear_button.grid(row=1)
backspace_button = Button(root, text='DEL', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12',
                          command=backspace)
backspace_button.grid(row=1, column=1)
modulus_button = Button(root, text='%', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12',
                        command=modulus)
modulus_button.grid(row=1, column=2)
divise_button = Button(root, text='/', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12',
                       command=divise)
divise_button.grid(row=1, column=3)
multiply_button = Button(root, text='*', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12',
                         command=multiply)
multiply_button.grid(row=2, column=3)
sub_button = Button(root, text='-', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12', command=sub)
sub_button.grid(row=3, column=3)
add_button = Button(root, text='+', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12', command=add)
add_button.grid(row=4, column=3)
answer_button = Button(root, text='=', relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12',
                       bg='light goldenrod yellow', command=equal)
answer_button.grid(row=5, column=3)

# digit buttons and comma button
for digit in digits:
    digit_button = Button(root, text=digit, relief='raised', height=2, width=15, padx=5, pady=5, font='Times 12 bold',
                          command=lambda num=digit: number(num))
    digit_button.grid(row=row, column=col)
    row += 1
    if row > 4:
        row = 2
        col += 1
zero_button = Button(root, text='0', relief='raised', height=2, width=33, pady=5, font='Times 12 bold', command=zero)
zero_button.grid(row=5, columnspan=2)
comma_button = Button(root, text='.', relief='raised', height=2, width=16, pady=5, font='Times 12 bold', command=comma)
comma_button.grid(row=5, column=2)

# root mainloop
root.mainloop()
