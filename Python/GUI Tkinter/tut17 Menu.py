
from tkinter import *

root = Tk()
root.geometry("789x654")
root.title("Pycharm Community Edition")

def myfunc():
    print("I am the function which is in file menu")

# Use this to create non drop down menu
#Menu is put in root
# mainmenu = Menu(root)
# mainmenu.add_command(label="File", command=func_file)
# mainmenu.add_command(label="Exit", command=quit)
# # config is similar to pack the menu
# root.config(menu=mainmenu)

# Create a mainmenu horizontly
mainmenu = Menu(root)

# Create a submenu varticaly
m1 = Menu(mainmenu, tearoff=0)
# tearoff is remove dottedline
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
# pack m1 menu in maninmenu under File
mainmenu.add_cascade(label="File", menu=m1)
# pack manimenu in root
root.config(menu=mainmenu)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_command(label="Paste", command=myfunc)
m2.add_separator()
m2.add_command(label="Find", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)


root.mainloop()
