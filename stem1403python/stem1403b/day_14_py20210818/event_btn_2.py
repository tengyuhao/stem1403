"""
Event binding
"""

from tkinter import *


def handler(event):
    print(f"I was clicked via bind(). {event.x} {event.y}")


root = Tk()
root.title("Demo of Button and CLick")
root.geometry("640x480+300+300")
root.config(bg="white")

# command option
label1 = Label(root, text="Click me")
label1.pack()

label1.bind('<Button-2>', handler)

# no stop to receive the update
root.mainloop()
