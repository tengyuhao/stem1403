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
from tkinter import messagebox as msg
from tkinter.ttk import Separator
# import sys

username = "admin"
password = "123456"
# title for message box
title = "Show messagebox"


def callback():
    if usernameE.get() == username:
        if passwordE.get() == password:
            text = "Welcome to our platform."
            msg.showinfo(title, text)

        else:
            text = "Sorry, your password is not correct."
            msg.showerror(title, text)

    else:
        text = "Sorry, your username or your password is not correct."
        msg.showerror(title, text)
        # sys.exit()


root = Tk()
root.title("Python GUI - Homework")
root.geometry("480x160")
# root.config(bg="black")

titleL = Label(root, text="Login Form", font=("SF Pro Display", 20, "bold"), padx=10, pady=15).grid(row=0, column=1)

sep1 = Separator(root, orient=HORIZONTAL)
sep1.grid(sticky=N, row=3, column=1, pady=5)

usernameL = Label(root, font=("SF Pro Display", 15), text="Account")
usernameL.grid(row=4, padx=(50, 5), sticky='e')

passwordL = Label(root, text="Password", font=("SF Pro Display", 15))
passwordL.grid(row=6, padx=(50, 5), sticky='e')

try:
    usernameE = Entry(root, font=("SF Pro Display", 15))
    usernameE.grid(row=4, column=1, padx=(5, 20), columnspan=3)

    passwordE = Entry(root, show="*", font=("SF Pro Display", 15))
    passwordE.grid(row=6, column=1, padx=(5, 20), columnspan=3)

except Exception as e:
    print(e)

btn_login = Button(root, text="Login", font=("SF Pro Display", 15), command=callback)
btn_login.grid(row=12, column=1, sticky="w", padx=10, pady=10)

btn_quit = Button(root, text="Quit", font=("SF Pro Display", 15), command=c)
btn_quit.grid(row=12, column=2, sticky="we", padx=10, pady=10)

sep2 = Separator(root, orient=HORIZONTAL)
sep2.grid(sticky=N)

root.mainloop()



