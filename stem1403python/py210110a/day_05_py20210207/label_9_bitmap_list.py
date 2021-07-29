"""
"""

import tkinter as tk
# from tkinter import *
root = tk.Tk()
root.title('Python GUI - label')
winw = 800
winh = 600
posx = 300
posy = 200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddff77')

# create a label
mytext = 'My Text Label bitmap'

bitmap_list = ['error', 'info', 'error', 'info', 'error', 'info', 'error', 'info', 'error', 'info']
label_list = []

for i in range(10):
    mylabel = tk.Label(root, bg='white', bitmap=bitmap_list[i], padx=20, pady=10)
    label_list.append(mylabel)
    mylabel.pack()

#
#
# label1 = tk.Label(root,bg='white',bitmap = 'error',padx = 20, pady= 10)
# label2 = tk.Label(root,bg='white',bitmap = 'info',padx = 20, pady= 10)
# label3 = tk.Label(root,bg='white',bitmap = 'questhead',padx = 20, pady= 10)
# label4 = tk.Label(root,bg='white',bitmap = 'question',padx = 20, pady= 10)
# label5 = tk.Label(root,bg='white',bitmap = 'warning',padx = 20, pady= 10)
# label6 = tk.Label(root,bg='white',bitmap = 'gray75',padx = 20, pady= 10)
# label7 = tk.Label(root,bg='white',bitmap = 'hourglass',padx = 20, pady= 10)
# label8 = tk.Label(root,bg='white',bitmap = 'gray50',padx = 20, pady= 10)
# label9 = tk.Label(root,bg='white',bitmap = 'gray25',padx = 20, pady= 10)
# label10 = tk.Label(root,bg='white',bitmap = 'gray12',padx = 20, pady= 10)
#
# # display labels
# for i in range(1, 11):
#     obj = 'label' + str(i)
#     eval(obj).pack()
#
# res = eval('1+2*3')
# print(res)

root.mainloop()