'''
Label(): A Label is a Tkinter Widget class, which is used to display text or an image. The label is a widget that the user just views but does not interact with.

Geometry(): This method is used to set the dimensions of the Tkinter window and is used to set the position of the main window on the user’s desktop.

Minsize(): This method is used to set the minimum size of the Tkinter window. Using this method user can set the window’s initialized size to its minimum size, and still be able to maximize and scale the window larger.

Maxsize(): This method is used to set the maximum size of the Tkinter window i.e. maximum size a window can be expanded. Users will still be able to shrink the size of the window to the minimum possible.
'''
from tkinter import *

basic = Tk()

# geometry is used for when the screen is pop up in starting it display that size.
# width x height
basic.geometry("272x452")

# mixsize take minimum size of window of tkinter
# width, height
basic.minsize(150, 300)

# maxsize take maximum size of window of tkinter
# width, height
basic.maxsize(965, 635)


name = Label(text = "Keyur is a good boy.")
# without label packing doesn't show
name.pack()

basic.mainloop()