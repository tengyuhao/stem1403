"""
set min size for a window

minsize != minimize
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

time.sleep(3)

# set iconify
root.iconify()


root.mainloop()
