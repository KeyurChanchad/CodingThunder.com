from tkinter import *

def submit():
    print(f"Username : {uservalue.get()}")
    print(f"Password : {passentry.get()}")

def cancel():
    uservalue.set("")
    passvalue.set("")

root = Tk()
root.geometry("533x243")

user = Label(root, text="Username:")
password = Label(root, text="Password:")

# pack user and password by grid. grid take row and column by default it take 0
user.grid()
password.grid(row=1)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=2, pady=6, padx=10)
passentry.grid(row=1, column = 2)

Button(text="Submit", fg="white", bg="black", borderwidth=3, relief=RIDGE, padx=15, command=submit).grid(row =3, padx=15)
Button(text="Cancel", fg="white", bg="red", borderwidth=3, relief=RIDGE, padx=15, command=cancel).grid(row=3, column=2)

root.mainloop()