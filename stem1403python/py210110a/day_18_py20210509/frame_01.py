"""
Container
Frame
"""

from tkinter import *

root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry('640x480+300+200')
root.config(bg="#ddddff")

frameUpper = Frame(root, bg="lightgreen", height=30, width=205)
frameUpper.pack()

btnRed = Button(frameUpper, text="Red", fg="red").pack(side=LEFT)
btnGreen = Button(frameUpper, text="Green", fg="green").pack(side=LEFT)

frameLower = Frame(root, bg="lightgreen", height=30, width=150)
frameLower.pack(fill=BOTH, expand=True)

btnPurple = Button(frameLower, text="Purple", fg="purple").pack(side=TOP)
root.mainloop()
