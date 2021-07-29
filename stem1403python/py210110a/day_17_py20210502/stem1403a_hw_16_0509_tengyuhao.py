"""
Date : 2021-05-02
Rewrite and try out Checkbutton
Understanding the sample code above
Due date: By the end of next Sat.
"""

from tkinter import *


def selection_box():
    selection = ""
    for i in checkboxes:
        if checkboxes[i].get() == True:
            selection += roles[i] + "\t"
    settxt = "Your role(s) is/are : " + selection

    txt.set(settxt)
    if selection == "":
        txt.set("Please chose your role !")


root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry('640x480+300+200')

# Radiobutton
titleL = Label(root, text="Your role", bg="lightyellow", width=30, font=('SF Pro Display', 20))
titleL.pack()

roles = {0: 'Mage', 1: 'Warrior', 2: 'Archer'}
checkboxes = {}
for i in range(len(roles)):
    checkboxes[i] = BooleanVar()
    Checkbutton(root, text=roles[i], command=selection_box, variable=checkboxes[i]).pack()

txt = StringVar()
label1 = Label(root, textvariable=txt, font=('SF Pro Display', 20))
label1.pack()

root.mainloop()
