"""
Button
state

normal
active
disabled
"""
from tkinter import *


def changeColor(bgColor):
    root.config(bg=bgColor)


root = Tk()
root.title('Python GUI - Button and Lambda')
root.geometry('300x200+300+200')


# create a button using lambda
color11 = "blue"
color1 = Button(root, text="blue", height=2, width=5, font=('SF Pro Display', 15),
                bg='white', command=lambda: changeColor(color11), state='normal')
color1.pack(anchor=S, side=RIGHT, padx=5, pady=5)

# create a button object
color22 = "yellow"
color2 = Button(root, text='yellow', height=2, width=5, font=('SF Pro Display', 15), bg='white',
                command=lambda: changeColor(color22), state='disabled')
color2.pack(anchor=S, side=RIGHT, padx=5, pady=5)

# create a button for closing and to exit
btn2 = Button(root, text='Close', command=root.destroy, height=2, width=5, font=('SF Pro Display', 15),
              bg='white', state='active')
btn2.pack(anchor=S, side=RIGHT, padx=5, pady=5)

root.mainloop()
