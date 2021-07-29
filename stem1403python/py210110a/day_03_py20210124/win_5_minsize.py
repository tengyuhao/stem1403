"""
set min size for a window

minsize != minimize
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
# root.maxsize()
root.minsize()

# case 2.
root.minsize(300, 300)

root.mainloop()
