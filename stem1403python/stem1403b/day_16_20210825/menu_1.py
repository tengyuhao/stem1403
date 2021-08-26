"""
menu

basic menu and menu option
"""

from tkinter import *
from tkinter import messagebox


def test_menu1():
    messagebox.showinfo("Test", "Menu 1 was clicked")


def test_menu2():
    messagebox.showinfo("Test", "Menu 2 was clicked")


root = Tk()
root.title("Menu")
root.geometry("640x480+300+300")

menubar = Menu(root)
menubar.add_command(label="Menu_1", command=test_menu1)
menubar.add_command(label="Menu_1", command=test_menu2)
menubar.add_command(label="Exit", command=root.destroy)

# set menu
root.config(menu=menubar)

root.mainloop()
