import tkinter
import PIL.Image , PIL.ImageTk
import cv2
from functools import partial
import threading    # If your program may block it handle by tread
import imutils      # It resize the Image
import time

stream = cv2.VideoCapture("C:\\Users\\Lenovo\\Desktop\\clip.mp4")
flag = True

def play(speed):
    global  flag
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)   # it get the speed
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed) # it increase or decrease speed

    grabbed, frame = stream.read()   # grabbed - if stream read successful it return true and in frame - stream
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor = tkinter.NW)

    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag

    print(f"The video is play at {speed}x")

def pending(decision_play):
     # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("C:\\Users\\Lenovo\\Desktop\\pending.png"), cv2.COLOR_BGR2RGB)   #read image and convert to color image
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)   # resize image
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))    # read image as array convert to tkinter compatiable image
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 2. Wait for 1 second
    time.sleep(3)

     # 3. Display sponsor image
    frame = cv2.cvtColor(cv2.imread("C:\\Users\\Lenovo\\Desktop\\sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

     # 4. Wait for 1.5 second
    time.sleep(2.5)

     # 5. Display out/notout image
    if decision_play == 'out':
        decisionImg = "C:\\Users\\Lenovo\\Desktop\\out.png"
    else:
        decisionImg = "C:\\Users\\Lenovo\\Desktop\\not_out.png"

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)




def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")


# CAPITAL for Constant
SET_WIDTH = 650
SET_HEIGHT = 368

# tkinter gui
window = tkinter.Tk()
window.title("Third Umpire Decision Review")

#create canvas
canvas = tkinter.Canvas(window, width=SET_WIDTH, height= SET_HEIGHT)
cv_image = cv2.cvtColor(cv2.imread("C:\\Users\\Lenovo\\Desktop\\welcome.png"), cv2.COLOR_BGR2RGB)
# show photo on canvas
photo = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(cv_image))
image_no_canvas = canvas.create_image(0, 0, ancho = tkinter.NW, image = photo)
canvas.pack()

# command takes function that has no argument but if you want give argument then you partial. Partial take function and argument. command feel that it has no-argument func.
btn = tkinter.Button(window, text= "<< Previous (fast)",  width= 50, command = partial(play, -20))
btn.pack()

btn = tkinter.Button(window, text= "<< Previous (slow)",  width= 50, command =  partial(play ,-5))
btn.pack()

btn = tkinter.Button(window, text= "Next (fast) >>",  width= 50, command = partial(play, 20))
btn.pack()

btn = tkinter.Button(window, text= "Next (slow) >>", width= 50, command = partial(play, 5))
btn.pack()

btn = tkinter.Button(window, text= "Out", width= 50, command = out)
btn.pack()

btn = tkinter.Button(window, text= "Not Out",  width= 50, command = not_out)
btn.pack()

window.mainloop()
