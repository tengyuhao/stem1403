"""
label_11_relief

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
mytext = 'flat'
label1 = tk.Label(root,
                  bg='red', fg='#ffffff',
                  text=mytext, relief='flat',
                  padx=20, pady=15)
label1.pack()

mytext = 'groove'
label2 = tk.Label(root,
                  bg='yellow', fg='#222222',
                  text=mytext, relief='groove',
                  padx=20, pady=15)
label2.pack()
mytext = 'raised'
label3 = tk.Label(root,
                  bg='yellow', fg='#222222',
                  text=mytext, relief='raised',
                  padx=20, pady=15)
label3.pack()
mytext = 'ridge'
label4 = tk.Label(root,
                  bg='yellow', fg='#222222',
                  text=mytext, relief='ridge',
                  padx=20, pady=15)
label4.pack()
mytext = 'solid'
label5 = tk.Label(root,
                  bg='red', fg='#222222',
                  text=mytext, relief='solid',
                  padx=20, pady=15)
label5.pack()

mytext = 'sunken'
label6 = tk.Label(root,
                  bg='blue', fg='#222222',
                  text=mytext, relief='sunken',
                  padx=20, pady=15)
label6.pack()

root.mainloop()
