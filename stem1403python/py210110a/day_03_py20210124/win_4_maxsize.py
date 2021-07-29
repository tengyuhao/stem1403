"""
set max size for a window

"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - subtopic')
winw = 800
winx = 450
posx = 300
poxy = 200
root.geometry(f'{winw}x{winx}+{posx}+{poxy}')

# case 1.
root.maxsize()

# case 2.
root.maxsize(1600, 900)

root.mainloop()
