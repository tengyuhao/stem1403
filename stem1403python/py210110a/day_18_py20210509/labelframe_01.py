"""
create a window
then create tw of lames
each of them takes half of the window
one background="color"
the other bg="color2"
"""

from tkinter import *

root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry('640x480')    # width x height
root.config(bg="#ddddff")

roles = {0: 'Mage', 1: 'Warrior', 2: 'Archer'}
checkboxes = {}

labfrm = LabelFrame(root, text="Please choose your roles")

for i in range(len(roles)):
    checkboxes[i] = BooleanVar()
    Checkbutton(labfrm, text=roles[i], variable=checkboxes[i]).pack()

labfrm.pack()

root.mainloop()
