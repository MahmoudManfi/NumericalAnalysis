from tkinter import messagebox
from tkinter import *
from tkinter import scrolledtext


def printOurFile():
    try:
        with open("report.txt" , 'r') as file:
            content = file.read()
        # f = open("report.txt", "r")
        # content = f.read()
    except:
        messagebox.showwarning('Error', 'Error while opening the file')
        return

    window = Tk()
    window.title("Report")
    window.geometry('750x700')
    txt = scrolledtext.ScrolledText(window, width=700, height=750)
    txt.grid(column=0, row=0)
    txt.insert(INSERT, content)
    window.mainloop()
