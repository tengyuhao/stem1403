"""
to create a main window
to set a title
to set image icon
to set size
to set initial position
to set a background image
"""

import tkinter as tk

root = tk.Tk()

# setting
root.title('Python GUI - Title')
root.iconbitmap('IMG_2408.ico')

# root.geometry('800x450+50+50')
# root.geometry('800x450-200+200')
# root.geometry('800x450-200-200')

# print(root.winfo_screenwidth())
# print(root.winfo_screenheight())

#  ======

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

ww = 800
wh = 450

# init posx, posy
x = ws / 2 - ww / 2
y = hs / 2 - wh / 2

x = int(x)
y = int(y)

root.geometry(f'{ww}x{wh}+{x}+{y}')


# background color
root.configure(bg="#ddddff")


root.mainloop()

