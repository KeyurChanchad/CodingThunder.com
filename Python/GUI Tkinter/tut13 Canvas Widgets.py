
from tkinter import *
from PIL import Image, ImageTk
root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Keyur Ka GUI")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# The line goes from the point x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0, fill="red")

# To create a rectangle specify parameters in this order - coors of top left and coors of bottom right
can_widget.create_rectangle(30, 50, 500, 150, fill="blue")

can_widget.create_text(200, 200, text="python", font="sanserif 16 italic")

can_widget.create_oval(344,233,244,355)
can_widget.create_oval(600, 300, 800, 400, fill="orange")

# can_widget.create_polygon(300,250, 0,450, 600, 450)  #Triangle

photo = ImageTk.PhotoImage(file='bg.jpg')
can_widget.create_image(0, 0 , image=photo)


button1 = Button(root, text="Exit")
button3 = Button(root, text="Start")
button2 = Button(root, text="Reset")

# Display Buttons
button1_canvas = can_widget.create_window(100, 10,
                                       anchor="nw",
                                       window=button1)

button2_canvas = can_widget.create_window(100, 40,
                                       anchor="nw",
                                       window=button2)

button3_canvas = can_widget.create_window(100, 70, anchor="nw",
                                       window=button3)
root.mainloop()

