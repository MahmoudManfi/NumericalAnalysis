from tkinter import *
from RootFinder.Utils.Function import Function
from RootFinder.GUI.Plot import draw

class queries():
    def __init__(self,parent,eqn,excution_time,left,right):
        self.parent = parent
        self.eqn = eqn

        large_font = ('Verdana', 10)

        equation_label = Label(parent,text = 'the equation:',bg= 'black',fg='orange')
        equation_label.pack(fill = X,padx = 5)
        eqn_text = Text(parent,bg='black',fg='white')
        eqn_text.insert(INSERT,self.eqn.replace('*',''))
        eqn_text.config(state='disabled')
        eqn_text.pack(fill=X, padx=5)

        excution_time_label = Label(parent,text='excution time: '+ str(excution_time),bg='black',fg='orange',font=large_font)
        excution_time_label.pack(fill = X,padx = 5)

        label = Label(parent,text ='Enter the value to be calculated!',bg='black',fg='orange')
        label.pack(fill = X,padx = 5)

        self.entry = Entry(parent, font = large_font)
        self.entry.pack(fill = X,padx =5,pady=5)

        self.ans_label = Label(parent,bg= 'black',fg='white',font=large_font)
        self.ans_label.pack(fill = X,padx = 5, pady = 5)

        button = Button(parent,text='calculate',command=self.calculate,bg='black', fg='orange')
        button.pack(fill=X, padx=5, pady=5)

        self.func = Function(eqn)
        try:
            draw(eqn,left,right)
        except:
            print("can't draw!")

    def calculate(self):
        try:
            self.ans_label.configure(text= self.func.get_value_at(float(self.entry.get())),fg = 'orange')
        except:
            self.ans_label.configure(text='check you Entered valid value!',fg = 'red')



# o = Tk()
#
# queries(o,'x')
#
# o.mainloop()