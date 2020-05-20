from tkinter import *

Xentries = []
Yentries = []


def warn_error():
    label = Label(window, text='check you entered valid order!', bg='black', fg='red')
    label.pack()


def sumbit():
    global Xentries
    global Yentries
    Xvalues = []
    Yvalues = []
    for i in Xentries:
        try:
            Xvalues.append(int(i.get()))
        except:
            warn_error()
            return

    for i in Yentries:
        try:
            Yvalues.append(int(i.get()))
        except:
            warn_error()
            return
    # call function solver


def query(order):
    global  Xentries
    global Yentries
    for i in range(order):
        number_label = Label(window, text = i+1)
        number_label.grid(row = i, column = 0)
        Xentries.append(Entry(window).grid(row = i, column = 1))
        Yentries.append(Entry(window).grid(row = i, column = 2))

    button = Button(text = 'sumbit', command=sumbit, bg='black', fg='orange')






window = Tk()
query(5)








window.mainloop()






