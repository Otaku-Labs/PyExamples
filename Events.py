from tkinter import *
from tkinter import ttk

root = Tk()

def key_press(event):
    print("Type: {}".format(event.type))
    print("Widget: {}".format(event.widget))
    print("Char: {}".format(event.char))
    print("Keysym: {}".format(event.keysym))
    print("Keycode: {}".format(event.keycode))

def shortcut(event):
    print(event)

root.bind('<KeyPress>', key_press)
root.bind('<Control-x>', lambda e: shortcut("cut"))
root.bind('<Control-c>', lambda e: shortcut("copy"))
root.bind('<Control-v>', lambda e: shortcut("paste"))


root.mainloop()