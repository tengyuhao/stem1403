"""
Tkinter

get options of a widget

"""

from tkinter import *
root = Tk()
root.title('Python GUI - Cursors')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label widget
label1 = Label(root, text='keys',
               padx=30, pady=15,
               font = "Helnetic 20",
               bg='#72EFAA', fg='black',)
label1.pack()

list_keys = label1.keys()
for key in list_keys:
    print(key)

root.mainloop()


"""
activebackground
activeforeground
anchor
background
bd
bg
bitmap
borderwidth
compound
cursor
disabledforeground
fg
font
foreground
height
highlightbackground
highlightcolor
highlightthickness
image
justify
padx
pady
relief
state
takefocus
text
textvariable
underline
width
wraplength
"""