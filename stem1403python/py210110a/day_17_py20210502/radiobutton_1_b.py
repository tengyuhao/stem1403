"""
Radiobutton widget

Class 1. styling
activebackground
activeforeground
background
bd
bg
borderwidth
disabledforeground
fg
font
highlightbackground
highlightcolor
highlightthickness
foreground
offrelief
overrelief
relief
selectcolor
underline
width
wraplength

Class 2. layout
anchor
justify
height
padx
pady

Class 3. features (functionalities)
text
bitmap (context)
compound
command
cursor
image
selectimage

takefocus
textvariable

state
tristateimage
tristatevalue


value
variable

Class 4. other/misc
indicatoron

"""

from tkinter import *


def printOption():
    option = var.get()
    print(option)
    txt.set(option)



root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry('640x480+300+200')
root.config(bg="#ddcddf")

# Radiobutton
# var = StringVar
var = IntVar()
# var.set(None)
var.set(2)

radiobtn1 = Radiobutton(root, text="Warrior", command=printOption, variable=var, value=1)
radiobtn1.pack()

radiobtn2 = Radiobutton(root, text="Mage", command=printOption, variable=var, value=2)
radiobtn2.pack()

radiobtn3 = Radiobutton(root, text="Archer", command=printOption, variable=var, value=3)
radiobtn3.pack()


# use selected option
txt = StringVar()
txt.set("Please choose  a role")
label1 = Label(root, textvariable=txt, font=('SF Pro Display', 20))
label1.pack()


root.mainloop()
