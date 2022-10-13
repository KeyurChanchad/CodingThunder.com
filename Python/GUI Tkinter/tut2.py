'''
There are many graphical user interface (GUI) toolkits that you can use with the Python programming language. The big three are Tkinter, wxPython and PyQt.  A graphical user interface is an application that has buttons, windows, manu, submenu, scroll and lots of other widgets that the user can use to interact with your application.

There are other GUI
PySide 2, Kivy

Tkinter is famous library in python in web development
Kivy. This is the most preferred Python GUI framework which is used for computer and mobile applications
'''
# Note: There are currently 15 types of widgets in Tkinter. Button, Canvas, RadioButton, CheckButton, Menu, Frame, Label, etc. are different types of widgets used in Tkinter

# ~~~~~~~~~~~~~~~ Programme start here~~~~~~~~~~~~~~~~~~~~~
# First we need to import tkinter
from tkinter import *

# Create an instance of Tk class
root = Tk()

# gui logic here

# Run maninloop of tkinter
root.mainloop()

# This three things are required for build basic tkinter window
# Between the Tk() and mainloop() we build our logic
