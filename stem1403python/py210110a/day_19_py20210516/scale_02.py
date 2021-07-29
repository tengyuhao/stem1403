"""
Scale(parent, options, ...)

basic usage of Scale

get value via Scale object
"""

from tkinter import *


def changeNum(source):
    print("change value 1", var1.get())


def getNum():
    print("print value ", var1.get())


def setNum():
    var1.set(5)
    print("set value as", var1.get())


# main program
root = Tk()
root.title("Python GUI - Scale")
root.geometry("640x480")
# label
label = Label(root, text="Scale binding a variable", bg="lightyellow", width=30)
label.pack()
# var1 = IntVar()
var1 = IntVar()
scale1 = Scale(root, from_=0, to=10, orient=HORIZONTAL, variable=var1, command=changeNum)
scale1.pack()

Button(root, text="Get value", width=20, command=getNum).pack()
Button(root, text="Set value", width=20, command=setNum).pack()
root.mainloop()
