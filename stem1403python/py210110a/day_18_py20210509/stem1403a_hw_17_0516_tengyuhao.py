"""
Date: 2021-05-09
Design and implement a multiple option button list on the main window.
Click on each button to show a specific toplevel window.
The number of options should be at list 5.
Due date: by the end of next Sat.
"""


from tkinter import *


def MessageBox(msg):
    labTxt = msg
    topframe = Toplevel()
    topframe.geometry('300x180')
    topframe.title(labTxt)
    # print(labTxt, type(labTxt))
    Label(topframe, text=msg).pack(fill=BOTH, expand=True)


root = Tk()
root.title("Python GUI - Radiobutton")
root.geometry('920x480')    # width x height
root.config(bg="white")

msg = ["Recommender for you", "Shopping", "Shopping cart", "View the orders", "Shipping", "Setting"]
r = 1
c = 0
for msgBtn in msg:
    btn = Button(root, text=msgBtn, command=lambda msg=msgBtn: MessageBox(msg),
                 bg="white", padx=15, pady=15, height=1, width=15).grid(padx=15, pady=15, row=r, column=c)
    c += 1
    if c == 4:
        r += 1
        c = 0

root.mainloop()
