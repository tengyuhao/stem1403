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

root.geometry('800x450+50+50')
# root.geometry('800x450-200+200')
# root.geometry('800x450-200-200')

root.configure(bg="#ddddff")
# root.configure(bg="#ddffdd")
root.mainloop()
