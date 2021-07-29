"""
compound
"""


import tkinter as tk
root = tk.Tk()
root.title('Python GUI - label bitmap')
winw= 640
winh= 480
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddddff')
# create a label
mytext = 'compound left'
label1 = tk.Label(root,
                  bg='red', fg='#ffffff',
                  bitmap='question',
                  text=mytext, compound='left',
                  padx=20, pady=15)
label1.pack()
mytext = 'compound right'
label2 = tk.Label(root,
                  bg='yellow', fg='#222222',
                  bitmap='error',
                  text=mytext, compound='right',
                  padx=20, pady=15)
label2.pack()
mytext = 'compound top'
label3 = tk.Label(root,
                  bg='yellow', fg='#222222',
                  bitmap='gray75',
                  text=mytext, compound='top',
                  padx=20, pady=15)
label3.pack()
mytext = 'compound bottom'
label4 = tk.Label(root,
                  bg='yellow', fg='#222222',
                  bitmap='gray50',
                  text=mytext, compound='bottom',
                  padx=20, pady=15)
label4.pack()
mytext = 'compound center'
label5 = tk.Label(root,
                  bg='yellow', fg='#222222',
                  bitmap='gray25',
                  text=mytext, compound='center',
                  padx=20, pady=15)
label5.pack()
root.mainloop()