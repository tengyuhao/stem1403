"""
Tkinter
using grid layout
grid()
rowspan, columspan
merge cells

"""

from tkinter import *

root = Tk()
root.geometry('640x480+0+0')
root.config(bg='#959A9C')

# create label widgets
label1 = Label(root, text='Label 0,0', bg="yellow")
label2 = Label(root, text='Label 0,1')
label3 = Label(root, text='Label 1,0')

# show on screen
# column number is 0 by default
label1.grid(row=0, column=0, columnspan=2)
label2.grid(row=1, column=0)
label3.grid(row=1, column=1)

root.mainloop()
