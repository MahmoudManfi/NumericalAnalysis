from tkinter import *

from Bracketing import mainGUI

interval_list = []

class Interval(Frame):
    def __init__(self,parent,*args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.interval_list = []
        labelframe = Frame(self, padx=5, pady=5, bg='blue')
        labelframe.pack()

        from_label = Label(labelframe, text='From:', bg='blue')
        from_label.pack(side='left')

        self.leftInterval = Entry(labelframe)
        self.leftInterval.pack(side='left')

        entryframe = Frame(interval, padx=5, pady=5, bg='blue')
        entryframe.pack()

        to_label = Label(entryframe, text='To:', bg='blue')
        to_label.pack(side='left')

        rightInterval = Entry(entryframe)
        rightInterval.pack(side='left')
        button = Button(interval, text='Enter', command=self.sumbit_interval, bg='black', fg='orange')
        button.pack()


    def sumbit_interval(self):
        try:
            left = int(self.leftInterval.get())
        except:
            self.leftInterval.delete(0, END)
            self.warn_error()
            return
        try:
            right = int(self.rightInterval.get())
        except:
            self.rightInterval.delete(0, END)
            self.warn_error(interval)
            return
        if(left >= right):
            self.warn_error(interval)
            return
        interval.destroy()

        self.interval_list = [left,right]
        # print(interval_list[0],interval_list[1])


    def warn_error(self):
        label = Label(interval, text = 'check you entered valid intervals!', bg = 'black', fg = 'red')
        label.pack()



    # GUI Elements


    # interval = Tk()


    # interval.mainloop()


if __name__ == "__main__":
    interval = Tk()
    interval.title('Input the Interval')
    interval.configure(padx=4, pady=4, bg='blue')
    Interval(interval)
        # .pack(side="top", fill="both", expand=True)
    interval.mainloop()

