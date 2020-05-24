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
    window.geometry('1400x700')
    txt = scrolledtext.ScrolledText(window, width=1400, height=700)
    txt.pack()
    txt.insert(INSERT, content)
    window.mainloop()