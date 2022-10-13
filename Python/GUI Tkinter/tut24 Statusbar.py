
from tkinter import *

def upload():
    # set it ignor all and set last valur without update()
    statusvar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")
    # statusvar.set("Ready Keyur Hell of king")

root = Tk()
root.geometry("455x233")
root.title("Status bar tutorial")


statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvar=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command=upload).pack()
root.mainloop()
