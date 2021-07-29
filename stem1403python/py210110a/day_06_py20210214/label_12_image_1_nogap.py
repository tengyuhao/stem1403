"""
show an GIF image without any gap
"""

from tkinter import *

root = Tk()

root.title('Python GUI - subtopic')
root.config(bg='#ddddff')

# step 1. create an object of PhotoImage
photo_obj = PhotoImage(file='img/pimon.gif')

# step 2.
label1 = Label(root, image=photo_obj)

# step 3. place label with image into window
label1.pack()

root.mainloop()
