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


def printInfo1():
    print(rdbtn['text'])

def printInfo2():
    # print("I clicked")
    print(txt.get())


root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry('640x480+300+200')
root.config(bg="#ddcddf")

# Radiobutton
rdbtn = Radiobutton(root, text="Warrior", command=printInfo1)
rdbtn.pack()

txt = StringVar()
txt.set('Mage')
rdbtn2 = Radiobutton(root, text="Mage", command=printInfo2, textvariable=txt)
rdbtn2.pack()

# list all option
# for keys in rdbtn.keys():
#     print(keys)
# print(rdbtn.keys())

root.mainloop()
