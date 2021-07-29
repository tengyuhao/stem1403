"""
maximize window
"""

import tkinter as tk
import time

root = tk.Tk()
root.title('Python GUI - subtopic')
winw = 800
winx = 450
posx = 300
poxy = 200
root.geometry(f'{winw}x{winx}+{posx}+{poxy}')
root.update()

# maximize
root.state('zoomed')

def restore():
    print('restoring')
    root.state('normal')
    # root.update()

btn1 = tk.Button(root, text="Restore", command=restore)
btn1.pack()

root.mainloop()
