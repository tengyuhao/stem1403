"""
Date: 2021-03-08
1. Write a GUI program of clock
Requirements:
(Function)
Show current time in the pattern of HH:mm:ss.aaa
i.e.
10:12:45.369
(UI)
Display a title, main area for clock, and footer for the date
Due date: by the end of next Friday
Hint:
import datetime
strftime
white_check_mark
eyes
raised_hands

"""

import datetime
from tkinter import *
from tkinter.ttk import Separator


def time():
    digital_label.config(text=datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])
    digital_label.after(1, time)


# main program
root = Tk()
root.title('Clock')
winw = 500
winx = 245
posx = 200
poxy = 240
root.geometry(f'{winw}x{winx}+{posx}+{poxy}')
root.minsize(500, 245)
root.configure(bg="#959A9C")

# title
label_1 = Label(root,
                text="Clock",
                bg="#F0F0EC",
                fg="black",
                height=3,
                width=70,
                font=('SF Pro Text', 22, 'bold'),
                )
label_1.pack(padx=5, pady=5)

sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)

# Clock object
digital_label = Label(root,
                      bg="#6f926e",
                      fg="white",
                      height=3,
                      width=70,
                      font=('SF Pro Text', 22, 'bold'),
                      )
digital_label.pack(padx=15, pady=15)

time()

sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)

# footer
label_2 = Label(root,
                text="My clock 2021",
                bg="white",
                fg="black",
                height=3,
                width=140,
                font=('SF Pro Text', 11, 'bold'),
                )
label_2.pack()

root.mainloop()
