"""


"""

from tkinter import *


def showPwd():
    passwordE.config(show="")


def hidePwd():
    passwordE.config(show="*")


root = Tk()
root.title('Python GUI - Homework')
root.geometry('300x200')


accountL = Label(root, text="Account", font=('SF Pro Display', 15))
accountL.grid(row=2, padx=(50,5), sticky='e')

passwordL = Label(root, text="Password", font=('SF Pro Display', 15))
passwordL.grid(row=3, padx=(50,5), sticky='e')

accountE = Entry(root, width=20, font=('SF Pro Display', 15))
accountE.grid(row=2, padx=(50,5), column=1)
passwordE = Entry(root, width=20, font=('SF Pro Display', 15), show="*")
passwordE.grid(row=3, padx=(50,5), column=1)

showBtn = Button(root, text='Show password', command=showPwd)
showBtn.grid(row=4, column=1)

showBtn = Button(root, text='Hide password', command=hidePwd)
showBtn.grid(row=5, column=1)

root.mainloop()
