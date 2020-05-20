from tkinter import *

# Gui handler events
from RootFinder.GUI import Choosing_Interval_GUI
from RootFinder.GUI import Choosing_Method_GUI as methods
from RootFinder.GUI.Plot import draw


#
# root = Tk()
# root.withdraw()
# current_window = None
# def  replace_window(root):
#     """Destroy current window, create new window"""
#     global current_window
#     if current_window is not None:
#         current_window.destroy()
#     current_window = Toplevel(root)
#
#     # if the user kills the window via the window manager,
#     # exit the application.
#     current_window.wm_protocol("WM_DELETE_WINDOW", root.destroy)
#     return current_window

def solve_equation(function_string):

    print(function_string)


def get_equation():
    print(str(equation_entry.get()))
    return str(equation_entry.get())


def solve_button_handler():
    equation = equation_entry.get()
    solve_equation(equation)


def custom_solve_handler():
    methods.mainloop()
    print("custom solver is here ")


def draw_button_handler():
    eqn = get_equation()
    interval = Tk()
    interval.title('Input the Interval')
    interval.configure(padx=4, pady=4, bg='blue')
    i = Choosing_Interval_GUI.Interval(interval)
    # .pack(side="top", fill="both", expand=True)
    interval.mainloop()
    draw(eqn, i.interval_list[0], i.interval_list[1])


# Gui elements
window = Tk()
window.title("Root Finding")
window.geometry('500x500')
window.configure(bg='blue')

upFrame = Frame(window, bd=1, bg='black')
upFrame.pack(fill=X, padx=5, pady=5)

# label
label = Label(upFrame, text="Enter your function")
label.pack(fill=X)

# the space where we put the equation
large_font = ('Verdana', 20)
equation_entry = Entry(upFrame, font=large_font)
equation_entry.focus()
equation_entry.pack(fill=X)

buttonsframe = Frame(window, pady='10', bg='blue')
buttonsframe.pack()

# solve button
solve_btn = Button(buttonsframe, text="Solve", command=solve_button_handler, bg='black', fg='orange', pady='10')
# solve_btn.place(side =CENTER)
solve_btn.pack(fill=X)

# custom solve button (in case that the user want to choose a technique to solve the equation )
custom_solve_btn = Button(buttonsframe, text="custom Solve", command=custom_solve_handler, bg='black', fg='orange',
                          pady='10')
# custom_solve_btn.place(side =CENTER)
custom_solve_btn.pack(fill=X)

# drawing button
draw_btn = Button(buttonsframe, text="Plot", command=draw_button_handler, bg='black', fg='orange', pady='10')
draw_btn.pack(fill=X)

# list box to show steps
step_list = Listbox(window, height=200)
step_list.pack(side='bottom', fill=X)

# showing Gui elements in the window
window.mainloop()
