from datetime import datetime
from tkinter import *
from tkinter import filedialog
from Interpolation import interpolation
from Interpolation.GUI.Queries import queries
import os


class Point():
    def __init__(self, parent,order,var):
        self.parent = parent
        self.order = order
        self.var = var
        self.Xvalues = []
        self.Yvalues = []
        self.Xentries = []
        self.Yentries = []
        f = Frame(parent,bg= 'blue')
        f.pack(fill = X)
        label1 = Label(f,text='Enter the Points',bg = 'black',fg='orange')
        label1.grid(row = 0,columnspan = 3)
        label2 = Label(f,text='X', bg='blue', fg='black')
        label2.grid(row=1, column=1, pady=4)
        label3 = Label(f,text='Y', bg='blue', fg='black')
        label3.grid(row=1, column=2, pady=4)

        self.canvas = Canvas(parent, borderwidth=0, background='blue')
        self.frame = Frame(self.canvas, background="blue")
        scrollbar = Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(fill=BOTH, expand=True)
        self.frame_id = self.canvas.create_window((4, 2), window=self.frame, anchor='nw',tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        for k in range(order+1):
            number_label = Label(self.frame, text=k,bg='blue' )
            number_label.grid(row=k, column=0)
            self.Xentries.append(Entry(self.frame))
            self.Xentries[k].grid(row=k, column=1,padx = 4)
            self.Yentries.append(Entry(self.frame))
            self.Yentries[k].grid(row=k, column=2,padx = 4)

        # scrollbar.configure(command=frame.y)
        button = Button(parent,text='sumbit', command=self.sumbit, bg='black', fg='orange')
        button.pack(fill = X,pady = 4,padx = 5)

        choose_button = Button(parent,text='choose file', command=self.open_file, bg='black', fg='orange')
        choose_button.pack(fill = X,pady = 4,padx = 5)

        self.errorlabel = Label(parent,text='check you entered valid inputs!',bg='black',fg='red')

    def warn_error(self):
        self.errorlabel.pack(fill = X,pady= 3)

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
        self.solve()

        # call function solver

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.itemconfig(self.frame_id, height=event.height, width=event.width)


    def open_file(self):
        # self.parent.withdraw()
        condition = True
        while condition:
            file_path = filedialog.askopenfilename()
            condition = not file_path.__contains__('.txt')

        file = open(file_path, "r")
        for x in file:
            value = x.split(' ',1)
            try:
                self.Xvalues.append(int(value[0]))
                self.Yvalues.append(int(value[1]))
            except:
                  self.warn_error()
        self.solve()


    def solve(self):
        if not interpolation.check(self.Xvalues, self.Yvalues, self.order):
            self.warn_error()
            return
        self.parent.destroy()
        if self.var == 1:
            n = interpolation.Newton()
        else:
            n = interpolation.Lagrange()
        b = n.cal(self.Xvalues, self.Yvalues)
        excution_time_begin = datetime.now()
        # print(excution_time_begin)
        self.eqn = n.get_equ(self.Xvalues, b)
        # print(datetime.now())
        excution_time = datetime.now() - excution_time_begin
        # print(excution_time,type(excution_time))
        queries_GUI = Tk()
        queries_GUI.configure(bg='blue')
        queries(queries_GUI,self.eqn,excution_time)

        queries_GUI.mainloop()







#
# p = Tk()
# Point(p,4,1)
# p.mainloop()
#








