from tkinter import *

root = Tk()
root.geometry("789x654")
root.minsize(456, 123)

title = Label(root, text = "Button", bg = "cyan", fg = "brown", font = "sanserif 23 italic").pack()

f = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
f.pack(side="top", padx=12, pady=21)

def hello():
    print("I am print function")

def leptop_details():
    print(f'Lenovo G50 Dolby Audio Webcam ')

def age():
    print("My age is 20")

def name():
    print("I am keyur chanchad")

b1 = Button(f, text = "print now", command=hello, bg="orange", fg="white")
b1.pack(side='left', anchor='nw', padx=13,)

b2 = Button(f, text = "tell name", command=name, bg="orange", fg="white")
b2.pack(side='left', anchor='nw', padx=13,)

b3 = Button(f, text = "tell age", command=age, bg="orange", fg="white")
b3.pack(side='left', anchor='nw', padx=13,)

b4 = Button(f, text = "leptop details", command=leptop_details, bg="orange", fg="white")
b4.pack(side='left', anchor='nw', padx=13,)

root.mainloop()