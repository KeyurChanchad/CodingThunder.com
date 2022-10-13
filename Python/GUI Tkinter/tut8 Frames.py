
from tkinter import *
root = Tk()
root.geometry("655x333")
# Frame(root) means frame put in root, Frame is not itself visible
f1 = Frame(root, bg="grey", borderwidth=4, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, borderwidth=8, bg="grey", relief=RIDGE)
f2.pack(side=TOP, fill="x")

l = Label(f1, text="Project Tkinter - Pycharm")
l.pack(padx=3, pady=150)

l = Label(f2, text="Welcome to sublime text", font="Helvetica 16 bold", fg="red", pady=22)
l.pack()

root.mainloop()
