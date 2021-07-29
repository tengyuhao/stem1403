"""
refreshing

root.update
"""

import tkinter as tk

root = tk.Tk()
root.title('Python GUI - subtopic')
winw = 800
winx = 450
posx = 300
poxy = 200

root.geometry(f'{winw}x{winx}+{posx}+{poxy}')

# refeshin
root.update()

w = root.winfo_width()
h = root.winfo_height()
print(f'w={w}, h={h}')

root.mainloop()
