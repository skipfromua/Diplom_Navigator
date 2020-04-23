from tkinter import *

class Interface(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        


root = Interface()
root.mainloop()