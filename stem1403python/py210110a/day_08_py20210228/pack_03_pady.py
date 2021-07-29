"""

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


# Make it resizable

label1 = Label(root, text='Python', font=('Arial', 20))
label2 = Label(root, text='Java', bg='yellow', font=('Arial', 20))
label3 = Label(root, text='Web', font=('Arial', 20))
label4 = Label(root, text='Database', bg='yellow', font=('Arial', 20))

label1.pack(side=TOP, padx=20, pady=40)
label2.pack(side=TOP)
label3.pack(side=TOP)
label4.pack(side=TOP)

root.mainloop()