
from RootFinder.Utils import constants
from RootFinder.Utils.Function import Function as Func
from RootFinder.Utils.Formatter import Formatter as Formatter


def find_root_bisection(function_string, l, r):
    formatter = Formatter()
    formatter.add_entry("l", "r", "f(l)", "f(r)", "mid", "f(mid)")
    fun = Func(function_string)
    fl = fun.get_value_at(l)
    fr = fun.get_value_at(r)
    if fl * fr > 0:
        print("Sorry but Bisection method can not solve an equation with the given interval")
        return None
    print("eps ", constants.EPS)
    itr = 0
    while abs(r - l) > constants.EPS and itr < constants.MAX_ITERATIONS:
        m = l + (r - l) / 2
        fm = fun.get_value_at(m)
        print(l, r, fl, fr, m, fm, sep=' <><> ')
        formatter.add_entry(l, r, fl, fr, m, fm)
        if fm * fl > 0:
            l = m
        else:
            r = m
    if abs(r - l) > constants.EPS:
        print("Bisection method has iterated more than the maximum number of iterations ")
    formatter.display_steps()
    return (r + l) / 2
find_root_bisection("x + 19" , -100 , 100 )
# find_root_secant("cos(x) + x**2 - x - 4", -1.56,4)
# print(find_root_newton("x + 4", -3))
