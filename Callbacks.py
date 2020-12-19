import tkinter
from tkinter import ttk

RootWindow = tkinter.Tk()

def callback(n):
    print(f"In the callback for {n}")

ttk.Button(RootWindow, text = "Click Me 1", command = lambda: callback(1)).pack()
ttk.Button(RootWindow, text = "Click Me 2", command = lambda: callback(2)).pack()
ttk.Button(RootWindow, text = "Click Me 3", command = lambda: callback(3)).pack()

RootWindow.mainloop()
