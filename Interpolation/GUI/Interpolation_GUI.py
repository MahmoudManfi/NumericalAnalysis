from tkinter import *
from Interpolation.GUI.Points import Point

def warn_error():
    error_label.pack()


def sumbit():
    try:
        order = int(order_entry.get())
    except:
        warn_error()
        return
    print(order,var)
    Point_GUI = Tk()
    Point_GUI.configure(bg='blue')
    Point_GUI.geometry('1400x700')
    Point(Point_GUI,order,var)
    window.destroy()
    Point_GUI.mainloop()





window = Tk()
window.configure(bg= 'blue')


var = IntVar()
var.set(1)

metod_label = Label(window,text = 'choose the method',bg = 'black', fg= 'orange',pady= 4)
metod_label.pack(fill =X,padx = 4)

v = IntVar()
newton_button = Radiobutton(window, text='Newton Method',variable=var,value=1,pady='10',bg= 'blue')

newton_button.pack(fill=X)
lagrange_button = Radiobutton(window, text='Lagrange Method',variable=var,value = 2,pady='10',bg= 'blue')
lagrange_button.pack(fill=X)

order_label = Label(window,text = 'Enter the Order',bg = 'black', fg= 'orange',pady= 4)
order_label.pack(fill = X,padx = 4)

large_font = ('Verdana',20)
order_entry = Entry(window, font = large_font)
order_entry.pack(padx = 5, pady = 5)

button = Button(text = 'next',command = sumbit,bg = 'black', fg= 'orange')
button.pack(fill = X,padx= 5,pady = 5)

error_label = Label(window, text='check you entered valid order!', bg='black', fg='red')



window.mainloop()