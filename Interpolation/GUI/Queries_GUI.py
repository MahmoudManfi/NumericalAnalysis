from tkinter import *


class query():
    def __init__(self, parent,order):
        self.parent = parent
        self.oreder = order
        self.Xvalues = []
        self.Yvalues = []
        self.Xentries = []
        self.Yentries = []
        label1 = Label(parent,text='Enter the Points',bg = 'black',fg='orange')
        label1.grid(row = 0,columnspan = 3)
        label2 = Label(parent,text='X', bg='blue', fg='black')
        label2.grid(row=1, column=1, pady=4)
        label3 = Label(parent,text='Y', bg='blue', fg='black')
        label3.grid(row=1, column=2, pady=4)

        for self.i in range(2,order+3):
            number_label = Label(parent, text=self.i-1,bg='blue' )
            number_label.grid(row=self.i, column=0)
            self.Xentries.append(Entry(parent))
            self.Xentries[self.i-2].grid(row=self.i, column=1,padx = 4)
            self.Yentries.append(Entry(parent))
            self.Yentries[self.i-2].grid(row=self.i, column=2,padx = 4)

        button = Button(parent,text='sumbit', command=self.sumbit, bg='black', fg='orange')
        button.grid(row = self.i+1,columnspan=3,pady = 4)

        self.errorlabel = Label(parent,text='check you entered valid inputs!',bg='black',fg='red')

    def warn_error(self):
        self.errorlabel.grid(row =self.i+2,columnspan = 3,pady= 3)

    def sumbit(self):
        for entry in self.Xentries:
            try:
                self.Xvalues.append(int(entry.get()))
            except:
                self.warn_error()
                return

        for entry in self.Yentries:
            try:
                self.Yvalues.append(int(entry.get()))
            except:
                self.warn_error()
                return
        self.parent.destroy()
        # call function solver



















