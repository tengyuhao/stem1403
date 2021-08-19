"""
Button and Event handling

Event source 推送
Event - Mouse LMB - Single CLick
Event handling 处理事件
Event binding 事件
Gui is Event-driven programming
"""

from tkinter import *


def handler():
    print("I was clicked.")


root = Tk()
root.title("Demo of Button and CLick")
root.geometry("640x480+300+300")
root.config(bg="white")

# command option
btn1 = Button(root, text="Click me", command=handler)
btn1.pack()

# no stop to receive the update
root.mainloop()
