"""

"""

# import tkinter as tk
from tkinter import *
from tkinter.ttk import Separator

def start_counting(mylabel):
    print("entered start_counting")
    counter = 0


    def counting():

        nonlocal counter
        counter = counter + 1
        if counter > 10:
            mylabel.config(text="END")
        else:
            mylabel.config(text=str(counter))
            mylabel.after(1000, counting)

    counting()


# main program
root = Tk()
root.title('10-second timer')
winw = 640
winx = 245
posx = 200
poxy = 240
root.geometry(f'{winw}x{winx}+{posx}+{poxy}')
root.minsize(500, 245)
root.configure(bg="#959A9C")
label_1 = Label(root,
                text="10-second timer",
                      bg="#F0F0EC",
                      fg="black",
                      height=3,
                      width=70,
                      font=('SF Pro Text', 22, 'bold'))
label_1.pack(padx=5, pady=5)

sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)

# Label object
digital_label = Label(root,
                      bg="#F5DF4D",
                      fg="#326872",
                      height=3,
                      width=70,
                      font=('SF Pro Text', 22, 'bold'))
digital_label.pack(padx=15, pady=15)


start_counting(digital_label)

sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)

label_2 = Label(root,
                text="®2021 Yuhao Teng All rights reserved. Tous droits réservés. Verison 3.0",
                bg="white",
                fg="black",
                height=3,
                width=140,
                font=('SF Pro Text', 11, 'bold'))
label_2.pack()

root.mainloop()
