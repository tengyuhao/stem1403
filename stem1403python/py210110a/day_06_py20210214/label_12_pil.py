"""
image label with jpg
"""

from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title('Python GUI - Label image')

# root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')

# create a label with image in .jpg
img_obj = Image.open('img/xiao.jpg')

bgimg3 = ImageTk.PhotoImage(img_obj)


label3 = Label(root, image=bgimg3)
label3.pack()
root.mainloop()
