from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("789x665")
root.title("Slider")

def get_dollars():
    print(f'You have got {slider.get()} $')
    msg.showinfo(title='Amount Credited!', message=f'we have credited {slider.get()} in bank account')

# slider1 = Scale(root, from_=0, to=100)
# slider1.pack()

Label(root, text="How many dollar do you want?").pack()


slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
slider.set(10)
slider.pack()

Button(root, text='Get Dollars $$$', command=get_dollars).pack()
root.mainloop()