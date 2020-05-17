from tkinter import *
#
# def newton_handler():
#
#
# def lagrange_handler():
#     return
# command=newton_handler,
# command=lagrange_handler,

def warn_error():
    label = Label(window, text='check you entered valid order!', bg='black', fg='red')
    label.pack()


window = Tk()

metod_label = Label(window,text = 'choose the method',bg = 'black', fg= 'orange',pady= 4)
metod_label.pack()

v = IntVar()
newton_button = Radiobutton(window, text='Newton Method',variable=v,value=1,
                          pady='10')

newton_button.pack(fill=X)
lagrange_button = Radiobutton(window, text='Lagrange Method',variable=v,value = 2,
                             pady='10')
lagrange_button.pack(fill=X)

order_label = Label(window,text = 'Enter the Order',bg = 'black', fg= 'orange',pady= 4)
order_label.pack()

large_font = ('Verdana',20)
order_entry = Entry(window, font = large_font)
order_entry.pack()

try:
    order = int(order_entry.get())
except:
    warn_error()



window.destroy()

window.mainloop()