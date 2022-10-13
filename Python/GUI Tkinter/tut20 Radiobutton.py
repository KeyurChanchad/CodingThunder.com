from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry('615x456')
root.title('MessageBox')
var = StringVar()
var.set('Dosa')
def get_value():
    print(f'You have order {var.get()}')
    msg.askokcancel(title='Do you order now?', message=f'You have ordered {var.get()}')

Label(text='What would you like to have?', fg='blue', font="lucida 18 bold", pady=5).pack()

radio1 = Radiobutton(text='Dosa', variable=var, value="Dosa", padx=150, font='sanserif 11 italic').pack(anchor='w')
radio2 = Radiobutton(text='paratha', variable=var, value="Paratha",padx=150, font='sanserif 11 italic').pack(anchor='w')
radio3 = Radiobutton(text='pasta', variable=var, value="Pasta",padx=150, font='sanserif 11 italic').pack(anchor='w')
radio4 = Radiobutton(text='chakri', variable=var, value="Chakri",padx=150, font='sanserif 11 italic').pack(anchor='w')

Button(root, text='Order Now', command=get_value, padx=23, pady=9, fg='white', bg='black').pack()

root.mainloop()