from tkinter import *
from tkinter import ttk

root = Tk()

canvas = Canvas(root, width = 640, height = 480, background = "white")
canvas.pack()

def onClick(event):
    global previous
    previous = event
    print("Type: {}".format(event.type))
    print("Widget: {}".format(event.widget))
    print("Num: {}".format(event.num))
    print("X: {}".format(event.x))
    print("Y: {}".format(event.y))
    print("X root: {}".format(event.x_root))
    print("Y root: {}".format(event.y_root))

def draw(event):
    global previous
    canvas.create_line(previous.x, previous.y, event.x, event.y)
    previous = event

canvas.bind('<ButtonPress>', onClick)
canvas.bind('<B1-Motion>', draw)
canvas.clipboard_clear

root.mainloop()