"""
Button
clear content(Label)

cget()
"""

from tkinter import *


def msgShow():
    label["text"] = "Button Wiget"
    label["bg"] = "lightyellow"
    label["text"] = "blue"
    label['height'] = 5
    label['width'] = 15
    label['font'] = ('SF Pro Display', 15)

def msgClear():
    label["text"] = ""
    print(root.cget('bg'))
    label['bg'] = '#1d1d1f'


root = Tk()
root.geometry('1200x600+200+200')
root.config(bg='#1d1d1f')
root.title('Python GUI - Homework')

label = Label(root, bg="#1d1d1f")

# create a button
btn1 = Button(root, text='Click me!', command=msgShow, height=5, width=15, font=('SF Pro Display', 15),  bg='white')

# create a button for closing and to exit
btn2 = Button(root, text='Close', command=root.destroy,  height=5, width=15, font=('SF Pro Display', 15), bg='white')


# create a button for Clear message
btn3 = Button(root, text='Clear', command=msgClear,  height=5, width=15, font=('SF Pro Display', 15), bg='white')


label.grid(row=0, column=2, padx=50, pady=20)
btn1.grid(row=2, column=2, padx=50, pady=20)
btn2.grid(row=2, column=4, padx=20, pady=20)
btn3.grid(row=2, column=6, padx=50, pady=20)

root.mainloop()

