"""
create a label widget
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - Label')
winw = 640
winx = 480
posx = 300
poxy = 200
root.geometry(f'{winw}x{winx}+{posx}+{poxy}')

# create a label
label1 = tk.Label(root, text='My Text Label')

label1.pack()

root.mainloop()
