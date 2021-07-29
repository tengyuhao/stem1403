"""
my first GUI program
Tkinter

create a title for main window
"""

# import tkinter
from tkinter import *


# root.geometry('640x480')
try:
    root = Tk()
    root.title('Python GUI - My first GUI App')
    # 4:3 ratio
    # root.geometry('640x480')
    # root.geometry('800X600')
    root.geometry('800x600')

    # 16:9 ratio
    root.geometry('1200x900')
    root.mainloop()

except TclError as tcle:
    print(tcle)

except Exception as e:
    print(e)


