"""
[Homework] 2021-01-17
1. Create a main window with specified width and height
user may input width and height
2. Please center the window
3. Please add image icon to your window
"""

from tkinter import *
import sys as sys

try:
    ww = int(input("Please input the width : "))
    wh = int(input("Please input the height : "))
except Exception as e:
    print(e)
    sys.exit()

root = Tk()
root.title('Python GUI - Title')

try:
    root.iconbitmap('mylogo.ico')
except FileNotFoundError as fnfe:
    print(fnfe)
except Exception as e:
    print(e)

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()


# init posx, posy
x = ws / 2 - ww / 2
y = hs / 2 - wh / 2

x = int(x)
y = int(y)

root.geometry(f'{ww}x{wh}+{x}+{y}')

# background color
root.configure(bg="#ddddff")

root.mainloop()
