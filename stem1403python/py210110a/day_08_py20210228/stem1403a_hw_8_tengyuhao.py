"""
[Homework]
2021-02-28
Show and Hide a label in a window
Due date: By the end of next Sat.
"""

from tkinter import *


def hide_label(widget):
    return lambda: Pack.forget(widget)


def show_label(widget):
    return lambda: widget.pack(side=LEFT)


root = Tk()

root.title('Python GUI - homework 8')

root.geometry('640x480+0+0')
root.config(bg='#959A9C')

label1 = Label(root, text='Java 1', font=('SF Pro Display', 20), fg='black', bg="#F0F0EC")
label2 = Label(root, text='Python 2',  font=('SF Pro Display', 20), bg='yellow')
label3 = Label(root, text='Web 3', font=('SF Pro Display', 20), fg='white', bg='#83b5dd')

label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)

# hide label
label1.after(1000, hide_label(label1))

# show label
label1.after(2500, show_label(label1))

root.mainloop()
