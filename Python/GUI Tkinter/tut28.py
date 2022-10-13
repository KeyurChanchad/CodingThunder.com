from tkinter import *

root = Tk()
root.geometry("789x546")
root.title("Calculator")
# root.wm_iconbitmap('')
root.configure(bg='blue')

# bind widget take must one argument 'event'
def click(event):
    global snvar
    text = event.widget.cget('text')
    # print(text)
    if text == 'C':
        snvar.set("")
        screen.update()
    elif text == '=':
        pass
    else :
        snvar.set(text)
        screen.update()

snvar = StringVar()
snvar.set('')

screen = Entry(root, font = ('lucida', 34, 'bold'))
screen.pack(fill=Y, pady=20, ipadx=5, ipady= 2,)

# buttons = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0', '00', '%', '!', '.', '/', '*', '+', '-', '=', 'C']
# for i in range(0, 5):
f = Frame(root, bg="green")
b = Button(f, text='9', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind("", click)

b = Button(f, text='8', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('', click)

b = Button(f, text='7', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)

b = Button(f, text='6', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)

f.pack()


f = Frame(root, bg="green")
b = Button(f, text='5', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)

b = Button(f, text='4', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)

b = Button(f, text='3', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)

b = Button(f, text='2', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)
f.pack()

f = Frame(root, bg="green")
b = Button(f, text='1', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)

b = Button(f, text='0', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)

b = Button(f, text='00', font= 'lucida 29 bold')
b.pack(side=LEFT, padx=17, pady=3)
b.bind('<Button-1>', click)

b = Button(f, text='.', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)
f.pack()

f = Frame(root, bg="green")
b = Button(f, text='+', font= 'lucida 29 bold', padx=13)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)

b = Button(f, text='-', font= 'lucida 29 bold', padx=13)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)

b = Button(f, text='*', font= 'lucida 29 bold', padx=13)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)

b = Button(f, text='/', font= 'lucida 29 bold', padx=13)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)
f.pack()

f = Frame(root, bg="green")
b = Button(f, text='!', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)

b = Button(f, text='%', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)

b = Button(f, text='C', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)

b = Button(f, text='=', font= 'lucida 29 bold', padx=10)
b.pack(side=LEFT, padx=16, pady=3)
b.bind('<Button-1>', click)
f.pack()
root.mainloop()