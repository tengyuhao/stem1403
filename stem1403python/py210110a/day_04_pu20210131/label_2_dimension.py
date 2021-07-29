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
root.config(bg='#ddddff')
# create a label
label1 = tk.Label(root, text='My Text Label', width=50, height=3    )
label1.pack()

# create a label
label2 = tk.Label(root, text='My Text Label2', width=30, height=5)
label2.pack()

root.mainloop()
