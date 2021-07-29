"""
[Homework]
Date: 2021-03-28
Input N numbers from your keyboard
Put them into a list  (i.e. [1,3,5])
Create a window
Then place(add) N buttons to the window
anchor=S
side=LEFT, side=RIGHT
Button text is the current number you get
Create an 'Exit' button
which allows you to press it to close the window
Hint:
Lambda
pass parameter
only one callback function
Due date: by the end of next Sat.
white_check_mark
eyes
raised_hands
"""
from tkinter import *
import sys


def output(num):
    print(num, "is pressed")


list_num = []
try:
    while True:
        print("If you are finish, press #7867")
        number_input = input("Please input the number for the button : ")
        if number_input == "#7867":
            break
        else:
            list_num.append(number_input)
except Exception as e:
    print(f"It has some errors, Please try again. Error Description: {e}")
    sys.exit()

root = Tk()
root.title('Python GUI - Homework')
root.geometry('300x200+300+200')

for i in list_num:
    # create a button using lambda
    num_button = Button(root, text=i, height=2, width=5, font=('SF Pro Display', 15),
                        bg='white', command=lambda num=i: output(num))
    num_button.pack(anchor=S, side=LEFT, padx=5, pady=5)


# create a button for closing and to exit
btn2 = Button(root, text='Close', command=root.destroy, height=2, width=5, font=('SF Pro Display', 15), bg='white')
btn2.pack(anchor=S, side=RIGHT, padx=5, pady=5)

root.mainloop()

