from tkinter import *

# GUI class inherit from Tk
class GUI(Tk):
    def __init__(self):
        # super().__init__() is like root = Tk() Tk is super class
        super().__init__()
        self.geometry("744x377")

    def status(self):
        # root is as self
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def click(self):
        print("Button clicked")

    def createbutton(self, inptext):
        Button(text=inptext, command=self.click).pack()


if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbutton("Click me")
    window.mainloop()
    # window is root