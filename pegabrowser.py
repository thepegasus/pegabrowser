#!/usr/bin/python3
from tkinter import *

class pegaBrowser(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.hi=Button(self, text="Launch")
        self.hi.pack()

root=Tk()
root.wm_title("PegaBrowser - 0.1")
root.minsize(600,400)
pegabrowser=pegaBrowser(root)
pegabrowser.master.title=("PegaBrowser - 0.1")
pegabrowser.mainloop()
#print("Completed")
