"""
[Homework]
Date: 2021-02-07
1. Try out label widget
Description:
create a window based on previous homework
set icon, title, dimension, maxsize, minsize, bg and any other options for the window as much as you know
create at least 2 text Labels
set dimension, font, fg, bg, font and any other options you know.
create at least 2 bitmap Labels
set dimension, fg, bg, font and any other options you know.
Due date: by the end of next Friday
"""


from tkinter import *
import time

root = Tk()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()


# setting

# set a title
root.title('Python GUI - Kevin Teng\'s homework')

# set an image icon
try:
    root.iconbitmap('mylogo.ico')
except FileNotFoundError as fnfe:
    print(fnfe)
except Exception as e:
    print(e)

#  ====== Extra requirements =====

# specify dimension at 16:9
ww = 1600
wh = 900

# init posx, posy
x = ws / 2 - ww / 2
y = hs / 2 - wh / 2

x = int(x)
y = int(y)

# Make it at center point on your screen
root.geometry(f'{ww}x{wh}+{x}+{y}')

# Set a background color
root.configure(background="gray64")

# make it topmost
root.attributes('-topmost', True)

# Set max size and min size
root.maxsize(1600, 900)
root.minsize(300, 300)

# Make it resizable
root.resizable(True, True)

# text Label
# Label1
label1 = Label(root, text='Tkinter Label 1 ', font=('SF Pro Text', 22, 'bold'),
               height=10, width=20,
               anchor='nw',
               fg="white", bg="black")
# show on screen
label1.pack()

# Label2
label2 = Label(root, text='Tkinter Label 2', font=('SF Pro Text', 22, 'bold'),
               height=10, width=20,
               anchor='nw',
               fg='#a1a1a6', bg="black")

# show on screen
label2.pack()

# Bitmap Label
label1 = Label(root, width=30, height=3, bg='black', fg='white',
                bitmap='question',
                padx=20, pady=20)
label1.pack()

label2 = Label(root, width=30, height=3, bg='black', fg='#a1a1a6',
                bitmap='error',
                padx=20, pady=20)
label2.pack()
root.mainloop()


