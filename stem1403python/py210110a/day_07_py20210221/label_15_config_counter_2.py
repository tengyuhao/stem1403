"""
label counter 2

optimizing
optimization

optimize

refactor
refactoring

"""

# import tkinter as tk
from tkinter import *


def start_counting(mylabel):
    print("entered start_counting")

    counter = 0


    def counting():
        nonlocal counter
        counter = counter + 1

        mylabel.config(text=str(counter))

        mylabel.after(1000, counting)

    counting()


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


start_counting(digital_label)


root.mainloop()
