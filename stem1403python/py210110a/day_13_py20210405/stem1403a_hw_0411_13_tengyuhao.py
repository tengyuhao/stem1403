"""
[Challenge]  Project. Volume Controller
c04_button/button_03_b.py
Description
Max value and Min value
1. User can press '+' button to increase the number by one per click
2. User can press '-' button to decrease the number by one per click
3. The number shows in a Label
constraints:
the MAX value = 10,
the MIN value = -10,
default number = 0
default step number = 1,  step number is adjustable
"""

from tkinter import *

#
# The number who shows in the digital number
show_num = 0
maximum = 10
minimum = -10
# step_number = 1

try:
    step_number = input("Please input one step number : ")
    step_number = int(step_number)
    
except Exception as e:
    print("Sorry, your step number has some errors. So, we there were be -1 automatically.")
    step_number = 1
    print(e)


def addition():
    global show_num
    if show_num <= minimum:
        sub_button.config(state="normal")
    show_num = show_num + step_number
    if show_num >= maximum:
        add_button.config(state="disabled")
    digital_label.config(text="{}".format(show_num))


def subtraction():
    global show_num
    if show_num >= maximum:
        add_button.config(state="normal")
    show_num = show_num - step_number
    if show_num <= minimum:
        sub_button.config(state="disabled")
    digital_label.config(text="{}".format(show_num))


root = Tk()
root.title('Python GUI - Homework')
root.geometry('300x270+500+200')
root.config(bg="#0066cc")
root.resizable(1, 1)

digital_label = Label(text=show_num, font=('SF Pro Display', 35), width=25, height=5, bg="white")
digital_label.pack()

sub_button = Button(root, text="-", height=2, width=5, font=('SF Pro Display', 15),
                    bg='white', command=subtraction)
sub_button.pack(anchor=S, side=LEFT, padx=5, pady=5)


add_button = Button(root, text="+", height=2, width=5, font=('SF Pro Display', 15),
                    bg='white', command=addition)
add_button.pack(anchor=S, side=LEFT, padx=5, pady=5)


# create a button for closing and to exit
btn2 = Button(root, text='Close', command=root.destroy, height=2, width=18, font=('SF Pro Display', 15), bg='white')
btn2.pack(anchor=S, side=LEFT, padx=5, pady=5, fill=X)

root.mainloop()

