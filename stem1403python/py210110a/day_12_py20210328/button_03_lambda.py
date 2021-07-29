"""
Button
command
"""
from tkinter import *


def helloCallBack(num):
    if num == 1:
        mytext="This is a label widget 1."

    else:
        mytext="This is a label widget not 1."
    label1 = Label(root, text=mytext)
    label1.pack()
    # print('I was clicked.')

def helloCallBack_old(num):
    label1 = Label(root, text="This is a label widget.")
    label1.pack()
    print(num)
    # print('I was clicked.')

# main program
root = Tk()
root.title('Python GUI - Button and Lambda')
root.geometry('300x200+300+200')


# create a button using lambda
btn1 = Button(root, text="Lambda", command=lambda: helloCallBack(2))
btn1.pack()
# create a button object
btn2 = Button(root, text='OK', command=helloCallBack)
btn2.pack()
root.mainloop()