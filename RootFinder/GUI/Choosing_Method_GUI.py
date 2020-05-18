from tkinter import *

from RootFinder.Bracketing.Bisection import find_root_bisection
from RootFinder.Bracketing.FalsePosition import find_root_falsePosition
from RootFinder.OpenMethods.FixedPoint import find_root_fixedPoint
from RootFinder.OpenMethods.NewtonRaphson import find_root_newtonRaphson
from RootFinder.OpenMethods.Secant import find_root_secant
from RootFinder.GUI.Plot import draw

class Methods():
    def __init__(self,parent,function):
        self.parent = parent
        self.function = function
        bracketingMethods_label = Label(parent, text='Bracketing Methods')
        bracketingMethods_label.pack()

        bisection_button = Button(parent, text='Bisection Method', command = self.bisection_handler, bg='black', fg='orange',
                                  pady='10')
        bisection_button.pack(fill=X)

        falsePosition_button = Button(parent, text='False Position', command=self.falsePosition_handler, bg='black',
                                      fg='orange', pady='10')
        falsePosition_button.pack(fill=X)

        openMethods_label = Label(parent, text='Open Methods')
        openMethods_label.pack()

        fixedPoint_button = Button(parent, text='Fixed Point', command=self.fixedPoint_handler, bg='black', fg='orange',
                                   pady='10')
        fixedPoint_button.pack(fill=X)

        newtonRaphson_button = Button(parent, text='Newton Raphson', command=self.newtonRaphson_handler, bg='black',
                                      fg='orange', pady='10')
        newtonRaphson_button.pack(fill= X)

        secant_button = Button(parent, text='Secant', command=self.secant_handler, bg='black', fg='orange', pady='10')
        secant_button.pack(fill=X)




    def bisection_handler(self):
        interval_list = draw(self.function)
        find_root_bisection(self.function,interval_list[0],interval_list[1])
        Frame.destroy()


    def falsePosition_handler(self):
        interval_list = draw(self.function)
        find_root_falsePosition(self.function,interval_list[0],interval_list[1])
        Frame.destroy()

    def fixedPoint_handler(self):
        find_root_fixedPoint(self.function)
        Frame.destroy()

    def newtonRaphson_handler(self):
        find_root_newtonRaphson(self.function)
        Frame.destroy()

    def secant_handler(self):
        find_root_secant(self.function)
        Frame.destroy()



# m = Tk()
# Methods(m,"x")
# m.mainloop()