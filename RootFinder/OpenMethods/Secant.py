import RootFinder.Utils.constants as constants
from sympy import *
from RootFinder.Utils.Function import Function as Func
from RootFinder.Utils.Formatter import Formatter as Formatter


def find_root_secant(function_string, x_prev=0, x_cur=1):

    """
    :param x_prev:
    :param x_cur:
    :param function_string: the function given in string format
    :return: the value at which the function is zero (if exists )
    """
    formatter = Formatter()
    formatter.add_entry("Xprev", "Xcur", "F(Xprev)", "F(Xcur)", "Xnext")


    fun = Func(function_string)
    found = False
    f_prev = (fun.get_value_at(x_prev))
    f_cur = (fun.get_value_at(x_cur))
    for i in range(0, constants.MAX_ITERATIONS):
        r = f_cur * ((x_cur - x_prev) / (f_cur - f_prev))
        x_next = (x_cur - r)

        formatter.add_entry(x_prev, x_cur, f_prev, x_cur, x_next)
        #print(x_prev, x_cur, f_prev, f_cur, x_next, sep=' <><><> ')

        if abs(r) < constants.EPS:
            found = true
            break

        x_prev = x_cur
        f_prev = f_cur
        x_cur = x_next
        f_cur = round(fun.get_value_at(x_cur))


    if found == false:
        print("The method diverged , Try using another initial or make sure the function has a root and is continuous")
        return None
#    formatter.display_steps()
    return x_cur

#find_root_secant("exp(-x) - x " , 0 , 1 )