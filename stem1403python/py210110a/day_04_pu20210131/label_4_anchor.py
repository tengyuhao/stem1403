"""
anchor of a label widget

anchor = n, s, w, e, ne, nw, se, sw, center

anchor = N, S, W, E, NE, NW, SE, SW, CENTER
"""

# import tkinter as tk
from tkinter import *
root = Tk()
root.title('Python GUI - Label')
winw = 640
winx = 480
posx = 300
poxy = 200
root.geometry(f'{winw}x{winx}+{posx}+{poxy}')
root.config(bg='#ddddff')
# create a label
label1 = Label(root, text='My Text Label', width=50, height=3, anchor='nw')
label1.pack()

# create a label
label2 = Label(root, text='My Text Label2', width=30, height=5, anchor=NW)
label2.pack()

root.mainloop()
