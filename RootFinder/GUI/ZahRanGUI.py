from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from RootFinder.Utils import constants
from RootFinder.Bracketing import Bisection, FalsePosition
from RootFinder.OpenMethods import FixedPoint, NewtonRaphson, Secant
from RootFinder.GUI import Plot
from RootFinder.GUI import ZahRanReportGUI
from RootFinder.Utils import parsing, horner
from tkinter import scrolledtext
from tkinter import filedialog

# window
window = Tk()
window.title("Root Finder")
window.geometry('350x625')

# Entry
Label(window, text='Enter f(x) :').pack(anchor=S)
upFrame = Frame(window, bd=1, bg='black')
upFrame.pack(fill=X, padx=5, pady=5)
large_font = ('Verdana', 20)
equation_entry = Entry(upFrame, font=large_font)
equation_entry.focus()
equation_entry.pack(fill=X)

# Tabs
tabControl = ttk.Notebook(window)
chooseMethodTab = ttk.Frame(tabControl)
customMethodTab = ttk.Frame(tabControl)
plot = ttk.Frame(tabControl)
tabControl.add(chooseMethodTab, text='choose Method')
tabControl.add(customMethodTab, text='custom Method')
tabControl.add(plot, text='plot the function')
tabControl.pack()

# Tab1 Work Work Work
selected = IntVar()


def clicked():
    if selected.get() == 1 or selected.get() == 2 or selected.get() == 5:
        leftEntry['state'] = NORMAL
        rightEntry['state'] = NORMAL
        oneEntry['state'] = DISABLED
    elif selected.get() == 3 or selected.get() == 4:
        oneEntry['state'] = NORMAL
        leftEntry['state'] = DISABLED
        rightEntry['state'] = DISABLED
    else:
        oneEntry['state'] = DISABLED
        leftEntry['state'] = DISABLED
        rightEntry['state'] = DISABLED


def run():
    fun = equation_entry.get()
    ans = IntVar
    try:
        constants.EPS = float(epsEntry.get())
    except:
        messagebox.showwarning('Error', 'Error happened in the Epslon value, please enter again')
        return
    try:
        constants.MAX_ITERATIONS = int(iterationsEntry.get())
    except:
        messagebox.showwarning('Error', 'Error happened in the iterations value, please enter again')
        return
    if selected.get() == 1 or selected.get() == 2 or selected.get() == 5:
        try:
            left = float(leftEntry.get())
        except:
            messagebox.showwarning('Error', 'Error happened in the left value, please enter again')
            return
        try:
            right = float(rightEntry.get())
        except:
            messagebox.showwarning('Error', 'Error happened in the right value, please enter again')
            return
        if right <= left:
            messagebox.showwarning('Error', 'Right bound must be bigger than left bound')
            return
        try:
            if selected.get() == 1:
                ans = (Bisection.find_root_bisection(function_string=fun, l=left, r=right))
            elif selected.get() == 2:
                ans = (FalsePosition.find_root_falsePosition(function_string=fun, xl=left, xu=right))
            elif selected.get() == 5:
                ans = (Secant.find_root_secant(function_string=fun, x_prev=left, x_cur=right))
        except:
            messagebox.showwarning('Error', 'Error in calculations')
            return
    elif selected.get() == 3 or selected.get() == 4:
        try:
            initial = float(oneEntry.get())
        except:
            messagebox.showwarning('Error', 'Error happened in the initial value, please enter again')
            return
        try:
            if selected.get() == 3:
                ans = (FixedPoint.find_root_fixedPoint(function_string=fun, x=initial))
            elif selected.get() == 4:
                ans = (NewtonRaphson.find_root_newtonRaphson(function_string=fun, x=initial))
        except:
            messagebox.showwarning('Error', 'Error in calculations')
            return
    else:
        return

    if ans is not None:
        root.insert(INSERT, str(ans) + "\n")
        ZahRanReportGUI.printOurFile()


bisection = Radiobutton(chooseMethodTab, text='Bisection', value=1, variable=selected, command=clicked). \
    pack(anchor=W)
falsePosition = Radiobutton(chooseMethodTab, text='False Position', value=2, variable=selected, command=clicked). \
    pack(anchor=W)
fixedPoint = Radiobutton(chooseMethodTab, text='Fixed Point', value=3, variable=selected, command=clicked). \
    pack(anchor=W)
newton = Radiobutton(chooseMethodTab, text='Newton', value=4, variable=selected, command=clicked). \
    pack(anchor=W)
secant = Radiobutton(chooseMethodTab, text='Secant', value=5, variable=selected, command=clicked). \
    pack(anchor=W)
Label(chooseMethodTab, font=large_font, text='Initial Guesses').pack(anchor=S)
labelLeft = Label(chooseMethodTab, text='From :').pack(anchor=S)
leftEntry = Entry(chooseMethodTab, state='disabled')
leftEntry.pack(anchor=S)
labelRight = Label(chooseMethodTab, text='To :').pack(anchor=S)
rightEntry = Entry(chooseMethodTab, state='disabled')
rightEntry.pack(anchor=S)
labelOne = Label(chooseMethodTab, text='Initial :').pack(anchor=S)
oneEntry = Entry(chooseMethodTab, state='disabled')
oneEntry.pack(anchor=S)
Label(chooseMethodTab, text='Max Iterations :').pack(anchor=S)
iterationsEntry = Entry(chooseMethodTab)
iterationsEntry.insert(END, '50')
iterationsEntry.pack(anchor=S)
Label(chooseMethodTab, text='Eps :').pack(anchor=S)
epsEntry = Entry(chooseMethodTab)
epsEntry.insert(END, '0.00001')
epsEntry.pack(anchor=S)
btn = Button(chooseMethodTab, font=large_font, text="Run", command=run).pack(pady=10, anchor=S)
Label(chooseMethodTab, text='Root is', font=large_font, fg="red").pack(anchor=S)
root = scrolledtext.ScrolledText(chooseMethodTab, width=30, height=1)
root.pack(anchor=S)


# tab 2
def polySolver(f):
    try:
        constants.EPS = float(epsEntryForCustom.get())
        constants.MAX_ITERATIONS = int(iterationsEntryForCustom.get())
    except:
        messagebox.showwarning('Error', 'Error in eps or iterations values, try again')
        return
    try:
        b = horner.BirgeVieta()
        roots = b.cal(f, 1)
    except:
        messagebox.showwarning('Error', 'This can''t be solved with the given constrains or complex roots')
        return

    if len(roots) == 0:
        messagebox.showwarning('Error', 'complex roots')
        return
    root2.delete('1.0', END)
    for i in roots:
        root2.insert(INSERT, str(i) + "\n")


def randomSolve():
    try:
        polySolver(equation_entry.get())
    except:
        messagebox.showwarning('Error', 'Error in passing')
        return


Label(customMethodTab, text='**This way only works for polynomials').pack(pady=10, anchor=S)
Label(customMethodTab, text='Max Iterations :').pack(anchor=S)
iterationsEntryForCustom = Entry(customMethodTab)
iterationsEntryForCustom.insert(END, '50')
iterationsEntryForCustom.pack(anchor=S)
Label(customMethodTab, text='Eps :').pack(anchor=S)
epsEntryForCustom = Entry(customMethodTab)
epsEntryForCustom.insert(END, '0.00001')
epsEntryForCustom.pack(anchor=S)

Label(customMethodTab, text='Solve the written function :').pack(pady=10, anchor=S)
solve = Button(customMethodTab, font=large_font, text="Run", command=randomSolve) \
    .pack(anchor=S)
root2 = scrolledtext.ScrolledText(customMethodTab, width=30, height=1)
root2.pack(anchor=S)


# tab 3 plot
def plotFun():
    try:
        constants.PLOT_POINTS = float(plotPerI.get())
        Plot.draw(equation_entry.get(), float(plotFromEntry.get()), float(plotToEntry.get()))
    except:
        messagebox.showwarning('Error', 'Error happened in values, please enter again')
        return


plotFrom = Label(plot, text='From :').pack(anchor=S)
plotFromEntry = Entry(plot)
plotFromEntry.pack(anchor=S)
plotTo = Label(plot, text='To :').pack(anchor=S)
plotToEntry = Entry(plot)
plotToEntry.pack(anchor=S)
Label(plot, text='number of plot points :').pack(anchor=S)
plotPerI = Entry(plot)
plotPerI.pack(anchor=S)
plotPerI.insert(END, '50')
plotButton = Button(plot, font=large_font, text="Plot", command=plotFun).pack(pady=10, anchor=S)
window.mainloop()
