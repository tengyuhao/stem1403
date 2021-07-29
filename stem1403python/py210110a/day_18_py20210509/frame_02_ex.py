"""
create a window
then create tw of lames
each of them takes half of the window
one background="color"
the other bg="color2"
"""

from tkinter import *

root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry('640x480')    # width x height
root.config(bg="#ddddff")

frameUpper = Frame(root, bg="lightgreen", height=240, width=320)
frameUpper.pack(fill=BOTH, expand=True)


# Label(frameUpper, text="Label1", fg="white", bg="lightgreen").pack()
# Label(frameUpper, text="Label2", fg="white", bg="lightgreen").pack()


Label(frameUpper, text="Label1", fg="white", bg="lightgreen").place(x=50, y=50)
Label(frameUpper, text="Label2", fg="white", bg="lightgreen").pack(relx=0.3, rely=0.5)

frameLower = Frame(root, bg="black", height=240, width=320)
frameLower.pack(fill=BOTH, expand=True)


Label(frameLower, text="Label1", fg="white", bg="black").grid(row=0, column=0)
Label(frameLower, text="Label2", fg="white", bg="black").pack(row=0, column=1)

root.mainloop()