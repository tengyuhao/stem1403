"""
[Homework]
Date: 2021-01-24
Write a Python GUI program to create your own window
Common requirements:
1. set a title
2. set an image icon
Extra requirements:
1. specify dimension at 16:9
2. make it at center point on your screen
3. set a background color
4. make it topmost
5. set max size and min size
6. make it resizable
7. print out the initial height and width of your window at console
8. resizing your window
9. print out the current height and width of your window at console
"""

from tkinter import *
import time

root = Tk()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()


print("After 3s, the window will smaller automatic.")

# setting

# set a title
root.title('Python GUI - Title')

# set an image icon
try:
    root.iconbitmap('mylogo.ico')
except FileNotFoundError as fnfe:
    print(fnfe)
except Exception as e:
    print(e)

#  ====== Extra requirements =====

# specify dimension at 16:9
ww = 1200
wh = 900

# init posx, posy
x = ws / 2 - ww / 2
y = hs / 2 - wh / 2

x = int(x)
y = int(y)

# Make it at center point on your screen
root.geometry(f'{ww}x{wh}+{x}+{y}')

# Set a background color
root.configure(background="NavajoWhite1")

# make it topmost
root.attributes('-topmost', True)

# Set max size and min size
root.maxsize(1600, 900)
root.minsize(300, 300)

# print out the initial height and width of your window at console
print(f"initial width : {ww}")
print(f"initial height : {wh}")

# Make it resizable
root.resizable(True, True)

# resizing my windows
root.update()
time.sleep(3)

try:
    ww = 900
    wh = 700
    root.update()

    # init posx, posy
    x = ws / 2 - ww / 2
    y = hs / 2 - wh / 2

    x = int(x)
    y = int(y)

    # Make it at center point on your screen
    root.geometry(f'{ww}x{wh}+{x}+{y}')

except Exception as e:
    print(e)
root.update()

# print out the current height and width of your window at console
print(root.winfo_width())
print(root.winfo_height())

root.mainloop()

