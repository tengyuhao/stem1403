"""
Tkinter

a label counter

congig()
after()


def a function in another function
global scope, global variable
recursive function
high order function
"""


from tkinter import *


def run_counter(digit):
    """
    execute the counter and show current number on the Label
    :param digit: the Label with witch is display numbers
    :return:
    """
    def counting():

        global counter
        counter += 1
        digit.config(text=str(counter))
        digit.after(1000, counting)
    counting()


root = Tk()

root.title('Python GUI - Label position')
root.config(bg='#ddddff')

# label object
digital_label = Label(root,
               text='keys',
               padx=30,
               pady=15,
               font="Helnetic 20",
               bg='#72EFAA',
               fg='black',
               )
digital_label.pack()
counter = 0
run_counter(digital_label)
root.mainloop()
