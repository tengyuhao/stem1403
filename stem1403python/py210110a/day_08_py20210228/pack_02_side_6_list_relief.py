"""
"flat", "groove", "raised","ridge", "solid", "sunken
"""
from tkinter import *
import time

root = Tk()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# set a title
root.title('Python GUI - Layout pack')


# root.geometry(f'{ww}x{wh}+{x}+{y}')

# Set a background color
root.configure(bg="#ddddff")

reliefs = ["flat", "groove", "raised","ridge", "solid", "sunken"]
for i in reliefs:
    Label(root,
          text=i,
          fg="blue",
          font=('SF Pro Display', 20),
          relief=i).pack(side=LEFT, padx=20, pady=20)

root.mainloop()