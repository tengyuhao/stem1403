"""


"""

# import tkinter as tk
from tkinter import *


def start_counting():
    print("entered start_counting")

    global counter

    counter = counter + 1

    digital_label.config(text=str(counter))

    digital_label.after(1000, start_counting)


# main program
root = Tk()
root.title('Python GUI - Label counter')
winw = 640
winx = 480
posx = 200
poxy = 240
root.geometry(f'{winw}x{winx}+{posx}+{poxy}')
root.configure(bg="black")

# Label object
digital_label = Label(root,
                      bg="white",
                      fg="#a1a1a6",
                      height=3,
                      width=10,
                      font=('SF Pro Text', 22, 'bold'),
                      )
digital_label.pack()

counter = 0
start_counting()


root.mainloop()
