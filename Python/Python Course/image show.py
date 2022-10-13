# Python PIL | Image.show() method
# Last Updated : 17 Jul, 2019
# PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities. The Image module provides a class with the same name which is used to represent a PIL image. The module also provides a number of factory functions, including functions to load images from files, and to create new images.
#
# Image.sHOW() Displays this image. This method is mainly intended for debugging purposes.
# On Unix platforms, this method saves the image to a temporary PPM file, and calls the xv utility. On Windows, it saves the image to a temporary BMP file, and uses the standard BMP display utility to show it (usually Paint).
#
# Syntax: Image.show(title=None, command=None)
#
# Parameters:
#
# title – Optional title to use for the image window, where possible.
# command – command used to show the image
#
# Return Type = The assigned path image will open.







# importing Image class from PIL package
# from PIL import Image
# import  time
# print('opening a image')
# time.sleep(2)
# # creating a object
# im = Image.open(r"H:\old desktop\Interfacly\home2-300x300.png")
#
# im.show()
#
# print('opened')





# importing Image class from PIL package
from PIL import Image

# creating a object
im = Image.open(r'H:\old desktop\Interfacly\f2.jpg')

im.show()

