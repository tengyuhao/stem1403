"""
[Homework]
Date: 2021-03-21
Create a window with two buttons
Click one for showing a text content using a label
Click the other one to exit
Due date: by the end of next Saturday
"""

from tkinter import *

content = "This is my homework!"


def show_content():

    label_content.configure(text=content)


root = Tk()
root.geometry('1200x600+200+200')
root.config(bg='#1d1d1f')
root.title('Python GUI - Homework')

# create a button
btn1 = Button(root, text='Click me!', command=show_content, height=5, width=15, font=('SF Pro Display', 15), bg='white')
btn1.grid(row=2, column=2, padx=50, pady=20)

# create a button for closing and to exit
btn2 = Button(root, text='Close', command=root.destroy,  height=5, width=15, font=('SF Pro Display', 15), bg='white')
btn2.grid(row=2, column=4, padx=20, pady=20)

label_content = Label(root, height=5, width=60, font=('SF Pro Display', 15, 'bold'), bg='white')
label_content.grid(row=2, column=3, padx=50, pady=20)


root.mainloop()
