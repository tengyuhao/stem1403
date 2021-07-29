"""
Button

create a button
"""

from tkinter import *


# Hoist
def myresponse():
    print("I was clicked! ")


root = Tk()
root.geometry('600x480+200+200')
root.config(bg='#ddddff')
root.title('Python GUI - Button')

# create a button
# btn1 = Button(root, text='Click me!', command=myresponse())
btn1 = Button(root, text='Click me!', command=myresponse)
btn1.pack(padx=20, pady=20)

# create a button for closing and to exit
btn2 = Button(root, text='Close', command=root.destroy)
btn2.pack(padx=20, pady=20)

root.mainloop()
