from tkinter import *

def bisection_handler:



def falsePosition_handler:


def fixedPoint_handler:


def newtonRaphson_handler:


def secant_handler:




methods = Tk()
methods.title('choose the method type')


bracketingMethods_label = Label(methods, text = 'Bracketing Methods')
bracketingMethods_label.pack()

bisection_button = Button(methods, text = 'Bisection Method', command= bisection_handler ,bg= 'black',fg = 'orange', pady = '10')
bisection_button.pack(fill = X)

falsePosition_button = Button(methods, text = 'False Position', command=falsePosition_handler,bg= 'black',fg = 'orange', pady = '10')
falsePosition_button.pack(fill = X)

openMethods_label = Label(methods, text = 'Open Methods')
openMethods_label.pack()

fixedPoint_button = Button(methods, text = 'Fixed Point', command=fixedPoint_handler,bg= 'black',fg = 'orange', pady = '10')
fixedPoint_button.pack(fill = X)

newtonRaphson_button = Button(methods, text = 'Newton Raphson', command=newtonRaphson_handler,bg= 'black',fg = 'orange', pady = '10')
newtonRaphson_button.pack(fill = x)

secant_button = Button(methods, text = 'Secant', command=secant_handler,bg= 'black',fg = 'orange', pady = '10')
secant_button.pack(fill = X)

methods.mainloop()