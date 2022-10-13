from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry('615x456')
root.title('MessageBox')


def show():
    # a = msg.showerror(title='error massage', message="Error! Found 404")
    # a = msg.showinfo("msg title", "message dikhana click ok it return ok" )
    a = msg.askokcancel('ok cancel button', 'This is ok and cancel massage it return true and false')
    # a = msg.showwarning('show warning', 'it show warning return ok')
    # a = msg.askquestion('Question ask', 'Am i devil? yes or no')
    # a = msg.askyesno('ask yes no', 'Are you serious? return True False')
    # a = msg.askretrycancel('retry and cancel', 'Retry again later..')
    # a = msg.askyesnocancel('yes no cancel', 'Your computer virus exprired. Have you buy? ')
    print(a)

mainmenu = Menu(root)
# mainmenu.add_command(label="Click me to show message", command=show)
sub = Menu(mainmenu, tearoff=0)
sub.add_command(label = "Rate us", command=show)
sub.add_command(label = "Befriend ", command=show)
mainmenu.add_cascade(label="Help", menu=sub)
root.config(menu=mainmenu)

root.mainloop()