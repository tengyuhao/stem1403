"""
msg.showinfo(title, text)
"""
from tkinter import *
from tkinter import messagebox as msg
def helloCallBack():
    title = "Show messegebox"
    text = "Hello Python Tkinter"
    msg.showinfo(title, text)



root = Tk()
root.geometry("320x240+200+200")
root.config(bg="#ddddff")
root.title("Python GUI - Button Style")

btn1 = Button(root, text='Show Messagebox', command=helloCallBack, padx=50, pady=10)

btn2 = Button(root, text='Close', command=root.destroy)
btn1.grid(sticky=S, row=1, column=0, padx=(80, 0), pady=(160, 0))
btn2.grid(sticky=S, row=1, column=1, padx=(80, 0), pady=(160, 0))

root.mainloop()