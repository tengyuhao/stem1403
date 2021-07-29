"""
1. Writing a GUI program in Python tkinter for the registration process of a network application.

Basic requirements:
a. User can input a username
b. User can input a password
c. User can input a password for the second time to ensure user's password was input correctly
d. User can input a validation code (usually an integer) generated randomly by the System, and that code (or number)
should display on the window. If the user inputs the wrong code (or number), registration will fail and a messagebox
should popup on the screen to warn the user.
e. A text title for this application should be set properly on the interface. Note: It is not the title of the main
window.
f. A Button is required to perform registration once User finishes all inputs. Proper messages or information
is required to display in both cases of 'success' and 'failed'.
g. A second Button is required to perform reset (or clear all inputs on the window)
h. Another Button is required to perform closing window and exit

Hints:
Any layout manager is free to use.
To make a clean and concise layout for your GUI application.
Make a wireframe (or draft design) for your GUI
Assuming your application (program) is designed for a real scenario, therefore think about what previous experience you
had in other online registration processes.
"""
from tkinter import *
from tkinter import messagebox as msg
import random


# title for message box
title = "Show messagebox"
abc123_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w' 'x', 'y', 'z', '1', '2',
                       '3' '4', '5', '6', '7', '8', '9', '0']


def result():
    v1 = passwordE.get()
    v2 = usernameE.get()
    v3 = fNameE.get()
    v4 = lNameE.get()
    v5 = p_confirmE.get()
    v1.replace(" ", "")
    l1 = [v1, v2, v3, v4, v5]
    for i in l1:
        i.replace(" ", "")
        if len(i) == 0:
            text = "Sorry, miss something, please try again"
            msg.showerror(title, text)
            break

        else:

            if passwordE.get().strip() == p_confirmE.get().strip():
                if vCodeE.get().strip() == vCode_txt:
                    print(passwordE.get().strip())
                    text = f"Welcome {fNameE.get().strip()} ! Now you're the member of iPlatform"
                    msg.showinfo(title, text)
                    break
                else:
                    text = "Sorry, the validation code is not match please try again"
                    msg.showerror(title, text)
                    break

            else:
                text = "Sorry, your twos passwords do not match."
                msg.showerror(title, text)
                break


def clear():
    usernameE.delete(0, END)
    passwordE.delete(0, END)
    p_confirmE.delete(0, END)
    fNameE.delete(0, END)
    lNameE.delete(0, END)
    vCodeE.delete(0, END)


root = Tk()
root.title("Registration for our iPlatform")


# root.config(bg="black")

titleL = Label(root, text="Create your iPlatform Account", font=("SF Pro Display", 20, "bold"), padx=10, pady=15)
titleL.grid(row=0, columnspan=2)

usernameL = Label(root, font=("SF Pro Display", 15), text="Username : ")
usernameL.grid(row=2, padx=(50, 5), sticky='e')

passwordL = Label(root, text="Password : ", font=("SF Pro Display", 15))
passwordL.grid(row=3, padx=(50, 5), sticky='e')

# p = password
p_confirmL = Label(root, text="Confirm the password : ", font=("SF Pro Display", 15))
p_confirmL.grid(row=4, padx=(50, 5), sticky='e')

Label(root, text="We’re committed to protecting your data.",
      font=("SF Pro Display", 15, "bold")).grid(row=7, padx=(50, 5), columnspan=3)

fNameL = Label(root, text="First Name : ", font=("SF Pro Display", 15))
fNameL.grid(row=5, padx=(50, 5), sticky='e')

lNameL = Label(root, text="Last Name : ", font=("SF Pro Display", 15))
lNameL.grid(row=6, padx=(50, 5), sticky='e')

try:
    usernameE = Entry(root, font=("SF Pro Display", 15))
    usernameE.grid(row=2, column=1, padx=(5, 20), columnspan=3)

    passwordE = Entry(root, show="*", font=("SF Pro Display", 15))
    passwordE.grid(row=3, column=1, padx=(5, 20), columnspan=3)

    p_confirmE = Entry(root, show="*", font=("SF Pro Display", 15))
    p_confirmE.grid(row=4, column=1, padx=(5, 20), columnspan=3)

    fNameE = Entry(root, font=("SF Pro Display", 15))
    fNameE.grid(row=5, column=1, padx=(5, 20), columnspan=3)

    lNameE = Entry(root, font=("SF Pro Display", 15))
    lNameE.grid(row=6, column=1, padx=(5, 20), columnspan=3)

except Exception as e:
    print(e)

#  validation code
vCode = random.sample(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w' 'x', 'y', 'z', '1', '2',
                       '3' '4', '5', '6', '7', '8', '9', '0'], 4)
vCode_txt = f"{vCode[0]}{vCode[1]}{vCode[2]}{vCode[3]}"
# print(vCode_txt)

vCodeL = Label(root, text="Validation code : ", font=("SF Pro Display", 15))
vCodeL.grid(row=8, padx=(50, 5), sticky='e')
vCodeE = Entry(root, font=("SF Pro Display", 15))
vCodeE.grid(row=8, column=1, padx=(5, 20), columnspan=3)

infoL = Label(root,
              text=f"Make sure you are not robot, please input this validation code : {vCode_txt}".format(vCode_txt),
              font=("SF Pro Display", 15)).grid(row=9, column=0, padx=(5, 20), columnspan=3)

btn_login = Button(root, text="Login", font=("SF Pro Display", 15), command=result)
btn_login.grid(row=10, column=1, sticky="w", padx=10, pady=10)

btn_clear = Button(root, text="Clear", font=("SF Pro Display", 15), command=clear)
btn_clear.grid(row=10, column=3, sticky="w", padx=10, pady=10)

btn_quit = Button(root, text="Quit", font=("SF Pro Display", 15), command=root.destroy)
btn_quit.grid(row=10, column=2, sticky="we", padx=10, pady=10)


root.mainloop()

