from tkinter import *

root = Tk()
root.geometry('615x456')
root.title('MessageBox')

def add():
        global  i
        # ACTIVE which is select or active item before that add
        lstbox.insert(ACTIVE, f"Item - {i}")
        i += 1

i = 1
lstbox = Listbox(root)
lstbox.insert(END, "First Item")
lstbox.insert(END, "second Item")
lstbox.insert(END, "Third Item")
lstbox.pack()

Button(root, text="Add Item", command=add).pack()
root.mainloop()