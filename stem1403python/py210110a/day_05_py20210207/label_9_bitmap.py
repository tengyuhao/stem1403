"""
bitmap label
"error"			"info"
"questhead"	    "question"
"warning"		"hourglass"
"gray75"		"gray50"
"gray25"		"gray12"
"""
import tkinter as tk
# from tkinter import *
root = tk.Tk()
root.title('Python GUI - label')
winw= 800
winh= 600
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='black')

# create a label
mytext = 'My Text Label font'
label1 = tk.Label(root, text=mytext,
                  width=30, height=3,
                  bg='red', fg='#ffffff',
                  font = 'Helvetica 20 italic underline',
                  bitmap='question',
                  padx= 20, pady = 20)
label1.pack()

# create a label
mytext = 'My Text Label font'
label2 = tk.Label(root, text=mytext,
                  width=30, height=3,
                  bg='yellow', fg='#ffffff',
                  font = 'Helvetica 20 italic underline',
                  bitmap='error',
                  padx= 20, pady = 20)
label1.pack()

root.mainloop()
