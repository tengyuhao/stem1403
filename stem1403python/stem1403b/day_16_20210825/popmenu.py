"""
popup menu

menu_object.post() - show or pop up a popup-menu
event.x_root
event.y_root

v.s.
event.x
event.y

"""

from tkinter import *

def copy():
    print("copy")


def cut():
    print("cut")


def paste():
    print("paste")


def showPopupMenu(event):
    popupmenu.post(event.x_root, event.y_root)


root = Tk()
root.title("Athensoft Python Course | Popup Menu")
root.geometry("640x480+300+300")

# define a popup menu
popupmenu = Menu(root, tearoff=False)
popupmenu.add_command(label="Copy", command=copy)
popupmenu.add_command(label="Cut", command=cut)
popupmenu.add_separator()
popupmenu.add_command(label="Paste", command=paste)

# binding to root
root.bind("<Button-2>", showPopupMenu)

root.mainloop()




