
from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("CodeWithKeyur - Title Of My GUI")
# set icon of tkinter
# root.wm_iconbitmap("1.ico")

# change in tkinter gui
root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close", command = root.destroy).pack()

root.mainloop()
