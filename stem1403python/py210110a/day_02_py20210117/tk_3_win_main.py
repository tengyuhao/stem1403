"""
to create a main window
to set a title
to set image icon

.png
.img
.bmp
.gif

step 1. chose an image
square 32x32, 16x16

step 2. copy to working folder

step 3. convert to .ico
"""

import tkinter as tk

root = tk.Tk()

# setting
root.title('Python GUI - Title')
root.iconbitmap('IMG_2408.ico')

#  widget

root.mainloop()
