import pyautogui   #pip install pyautogui 
# pyautogui is for automated keyboard key and mouse
from PIL import Image, ImageGrab   # pip install pillow
# ImageGrab is for screenshort
import time
# from numpy import array, asarray
# asarray is just for show image as array

# pyautogui.keyDown("K")
# pyautogui.keyDown("e")
# pyautogui.keyDown("y")
# pyautogui.keyDown("u")
# pyautogui.keyDown("r")

def hitkey(key):
    pyautogui.keyDown(key)

def iscollied(data):
    for i in range(500, 520):
        for j in range(230, 265):
            if data[i, j] < 100:
                hitkey('up')
                return True
    
    for i in range(500, 515):
        for j in range(195, 217):
            if data[i, j] < 100:
                hitkey('down')
                return True

    return False

    


   
            


if __name__ == '__main__':
    print('Dino game start in 2 sec..')
    time.sleep(2)
    # hitkey('up')

    while True:
        image = ImageGrab.grab().convert('L')    # convert('L') is convert screenshort in gray color
        data = image.load()   # image.load( ) is convert image in array form
        # print(asarray(image))
        iscollied(data)

        # # # Draw the rectangle
        # for i in range(500, 520):
        #     for j in range(230, 265):
        #        data[i, j] = 0

        # # Draw the bird 
        # for i in range(500, 515):
        #     for j in range(195, 217):
        #          data[i, j] = 100
                
        # image.show()
        # break
    
    





