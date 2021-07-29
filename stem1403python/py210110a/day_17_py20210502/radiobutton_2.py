"""
Checkbutton

get()
using dictionary
variable, BooleanVar(

"""

from tkinter import *


def selection_box():
    selection = ""
    for i in checkboxes:
        if checkboxes[i].get() == True:
            selection += roles[i] + "\t"
    return selection

root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry('640x480+300+200')
root.config(bg="#ddcddf")

# Radiobutton


titleL = Label(root, text="Your role", bg="lightyellow", width=30, font=('SF Pro Display', 20))
titleL.pack()

roles = {0: 'Mage', 1: 'Warrior', 2: 'Archer'}
checkboxes = {}
for i in range(len(roles)):
    checkboxes[i] = BooleanVar()
    Checkbutton(root, text=roles[i], command=selection_box, variable=checkboxes[i]).pack()

root.mainloop()
