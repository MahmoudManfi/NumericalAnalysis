from tkinter import *
import tkinter as tk


# Gui handler events
def solve_equation(function_string):
    print(function_string)


def get_equation():
    print(str(equation_entry.get()))
    return str(equation_entry.get())


def solve_button_handler():
    equation = equation_entry.get()
    solve_equation(equation)


def custom_solve_handler():
    print("custom solver is here ")


def draw_button_handler():
    return None


# Gui elements
window = tk.Tk()
window.title("Root Finding")
window.geometry('500x500')

# label
label = tk.Label(text="Enter your function")
label.grid(row=0, column=0)

# the space where we put the equation
equation_entry = tk.Entry()
equation_entry.grid(row=1, column=0)

# solve button
solve_btn = tk.Button(text="Solve", command=solve_button_handler)
solve_btn.grid(row=2, column=0)

# custom solve button (in case that the user want to choose a technique to solve the equation )
custom_solve_btn = tk.Button(text="custom Solve", command=custom_solve_handler)
custom_solve_btn.grid(row=2, column=1)

# drawing button
draw_btn = tk.Button(text="Plot", command=draw_button_handler)
draw_btn.grid(row=2, column=2)

# list box to show steps
step_list = tk.Listbox(height=8, width=20)
step_list.grid(row=5, column=0, pady=3)

# showing Gui elements in the window
window.mainloop()
