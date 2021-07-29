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

label1 = Label(root, text='< Last', font=('Arial', 20), fg='red')
label2 = Label(root, text='Next >', bg='yellow', font=('Arial', 20))
label3 = Label(root, text='Min', font=('Arial', 20), fg='red')
label4 = Label(root, text='Max', bg='yellow', font=('Arial', 20))

label1.pack(anchor=S, side=LEFT)
label2.pack(anchor=S, side=LEFT)
label3.pack(anchor=N, side=RIGHT)
label4.pack(anchor=N, side=RIGHT)



root.mainloop()
