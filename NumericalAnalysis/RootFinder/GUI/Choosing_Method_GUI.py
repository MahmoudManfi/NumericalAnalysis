from tkinter import *

from RootFinder.Bracketing.Bisection import find_root_bisection
from RootFinder.Bracketing.FalsePosition import find_root_falsePosition
from RootFinder.OpenMethods.FixedPoint import find_root_fixedPoint
from RootFinder.OpenMethods.NewtonRaphson import find_root_newtonRaphson
from RootFinder.OpenMethods.Secant import find_root_secant

from RootFinder.GUI import Plot as Plot, Choosing_Interval_GUI as Interval


class Methods(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        bracketingMethods_label = Label(methods, text='Bracketing Methods')
        bracketingMethods_label.pack()
        bisection_button = Button(methods, text='Bisection Method', command=self.bisection_handler, bg='black',
                                  fg='orange',
                                  pady='10')
        bisection_button.pack(fill=X)
        falsePosition_button = Button(methods, text='False Position', command=self.falsePosition_handler, bg='black',
                                      fg='orange', pady='10')
        falsePosition_button.pack(fill=X)
        openMethods_label = Label(methods, text='Open Methods')
        openMethods_label.pack()
        fixedPoint_button = Button(methods, text='Fixed Point', command=self.fixedPoint_handler, bg='black',
                                   fg='orange',
                                   pady='10')
        fixedPoint_button.pack(fill=X)
        newtonRaphson_button = Button(methods, text='Newton Raphson', command=self.newtonRaphson_handler, bg='black',
                                      fg='orange', pady='10')
        newtonRaphson_button.pack(fill=X)
        secant_button = Button(methods, text='Secant', command=self.secant_handler, bg='black', fg='orange', pady='10')
        secant_button.pack(fill=X)

    def bisection_handler(self, function):
        i = Interval.mainloop()
        i
        interval = Interval.interval_list
        # Plot.draw(function, interval[0], interval[1])
        find_root_bisection()
        Frame.destroy()

    def falsePosition_handler(self):
        Interval.mainloop()
        find_root_falsePosition()
        Frame.destroy()

    def fixedPoint_handler(self):
        find_root_fixedPoint()
        Frame.destroy()

    def newtonRaphson_handler(self):
        find_root_newtonRaphson()
        Frame.destroy()

    def secant_handler(self):
        find_root_secant()
        Frame.destroy()


methods = Tk()
methods.title('choose the method type')
Methods(methods)
methods.mainloop()

