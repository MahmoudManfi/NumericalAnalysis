from tkinter import BOTTOM, BOTH
from tkinter import *

import matplotlib.pyplot as plt
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from RootFinder.Utils.Function import Function as Func
from RootFinder.Utils import constants


def draw_from_lists(xs, ys):
    """
    :param xs: the list of x's
    :param ys: the list of y's such that for all xi  --> yi = f(xi)
    :return: plotting the function in a new window
    """
    app = Tk()
    figure = Figure(figsize=(5, 5), dpi=100)
    figure.add_subplot(111).plot(xs, ys)
    canvas = FigureCanvasTkAgg(figure, master=app)
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
    toolbar = NavigationToolbar2Tk(canvas, app)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    app.mainloop()

    # plt.plot(xs, ys)
    # plt.show()


def draw(function_string, left, right):
    seg = (right - left) / constants.PLOT_POINTS
    fun = Func(function_string)
    xs = list()
    ys = list()
    while left < right:
        #print(left)
        xs.append(left)
        ys.append(fun.get_value_at(left))
        left += seg
    draw_from_lists(xs, ys)

#
# f = "x * x "
# n = 50000
# left = -200
# right = 200
# draw(f , left , right )
