from tkinter import *

root = Tk()
root.title("Python GUI - Homework")
root.geometry("640x480+0+0")

label1 = Label(root, text='Label 1', font=('Times', 25), bg="orange", fg='blue')
label2 = Label(root, text='Label 2', font=('Times', 25), bg="orange", fg="red")
label3 = Label(root, text='Label 3', font=('Times', 25), bg="orange", fg='yellow')

label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)

label1.after(2000, Pack.forget(label1))
label1.after(2000, label1.pack(side=LEFT))

root.mainloop()
