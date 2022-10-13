
# Create a gui window which takes as input width and height
# and upon clicking apply, it should be able to change its size accordingly

from tkinter import *

root = Tk()

def create_window():
    can_width = width_value.get()
    can_height= height_value.get()
    # root.geometry(f"{can_width}x{can_height}")
    canvas = Canvas(root, width=can_width, height=can_height)
    canvas.pack()


f0 = Frame(root, bg="orange", borderwidth = 6, relief = GROOVE , padx=6, pady=10)
f0.pack(side='top')
Label(f0, text="Enter Width:").grid(row=1, column=3)
Label(f0, text="Enter Height:").grid(row=2, column=3)

width_value = IntVar()
height_value = IntVar()

Entry(f0, textvariable=width_value).grid(row=1, column=5)
Entry(f0, textvariable=height_value).grid(row=2, column=5)

Button(text="Apply", command=create_window,padx=25, pady=5).pack()



root.mainloop()