__author__ = "Elizabeth Gardner"
__date__ = "3 February 2022"
# CSC 512: Professional Practice
# GUI Experiment

from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    root.title("Hello World")
    frame = ttk.Frame(root, padding=250)
    frame.grid()
    ttk.Label(frame, text="Hello World").grid(column=0, row=0)
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()

    # print("Hello world")


if __name__ == "__main__":
    main()
