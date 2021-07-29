"""

"""

from tkinter import *
from tkinter.ttk import Separator

# main program
root = Tk()
root.title('Python GUI- ')
winw = 500
winx = 245
posx = 200
poxy = 240
root.geometry(f'{winw}x{winx}+{posx}+{poxy}')

root.configure(bg="#959A9C")

colors = ["red", "orange", "yellow", "green","cyan", "blue", "purple"]
r = 0

for color in colors:

    # create text label
    label_left = Label(root, text=color, relief="groove", bg="white", fg="black",width=20,
                       padx=20, pady=20, font=('SF Pro Text', 11, 'bold'))

    label_left.grid(row=r, column=0)

    # create text label
    label_right = Label(root, relief="groove", bg=color, padx=80, pady=20)

    label_right.grid(row=r, column=1)

    r = r + 1

root.mainloop()

