"""
Layout manager:  pack()
side=LEFT
start from left side
from left to right
"""

from tkinter import *
root = Tk()
label1 = Label(root, text='Python 1', font=('Arial', 20), fg="red", bg="yellow")
label2 = Label(root, text='Java 2', bg='yellow', fg="red", font=('Arial', 20))
label3 = Label(root, text='Web 3', font=('Arial', 20))

root.geometry('640x480+0+0')
root.config(bg='#ddddff')
label1.pack(side=LEFT, fill=Y)
label2.pack()
label3.pack(fill=X)


root.mainloop()
