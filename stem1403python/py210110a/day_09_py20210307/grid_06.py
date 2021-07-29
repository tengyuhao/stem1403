"""
grid()

"""

from tkinter import *

root = Tk()
# root.geometry('640x480+0+0')
root.geometry('+400+300')
root.config(bg='#959A9C')

# create label widgets
label1 = Label(root, text='Label 1', bg="yellow")
label2 = Label(root, text='Label 2')
label3 = Label(root, text='Label 3')
label4 = Label(root, text='Label 4', bg="yellow")

# show on screen
# column number is 0 by default
label1.grid(row=0, column=0, padx=20, pady=10)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)

root.mainloop()
