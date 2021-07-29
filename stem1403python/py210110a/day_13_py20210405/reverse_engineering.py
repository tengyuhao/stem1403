"""
reverse engineering
1. evaluate the product/result (observe)
   outlook, metric, functionality
2. analyze the result
3. reproduce
4. assembly
5. test
6. deliver

engineering
1. idea
2. design/plan
3. implement
4. test
5. deliver

One label and three buttons :
In the label : Start number : 0
There are 3 buttons in the bottom side:
first one is for -2, second one is for +2, third one is for exit the program
If you click for fist button : start number will be -2, ...
The minimum of the number will be -10, and the max will be 10
"""
from tkinter import *
root = Tk()
root.title('Python GUI - Homework')
root.geometry('300x200+300+200')

btn2 = Button(root, text='Close', command=root.destroy, height=2, width=5, font=('SF Pro Display', 15), bg='white')
btn2.pack(anchor=S, side=RIGHT, padx=5, pady=5)
