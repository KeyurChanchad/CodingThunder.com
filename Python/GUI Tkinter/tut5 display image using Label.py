from tkinter import *
from PIL import Image, ImageTk   #pip install pillow
import os

root = Tk()

root.title('Keyur image gallery')
root.geometry('1000x1200')

# By tkinter
# tkinter take only png image
# photo = PhotoImage(file="keyur.png")
# image_label = Label(image=photo)
# image_label.pack()

# By PIL  for jpg image,
# image = Image.open('bg.jpg')
# image  =  ImageTk.PhotoImage(image)
# # image  =  ImageTk.PhotoImage(file = 'bg.jpg')
# photo_label = Label(image=image)
# photo_label.pack()


root.mainloop()