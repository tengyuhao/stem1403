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

# resizable
root.resizable(False, False)
root.resizable(True, False)
root.resizable(0, True)

root.mainloop()
