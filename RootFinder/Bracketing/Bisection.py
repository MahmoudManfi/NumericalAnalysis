from RootFinder.Utils import constants
from RootFinder.Utils.Function import Function as Func

digits = constants.DIGITS;


def find_root_bisection(function_string, l, r):
    fun = Func(function_string)
    fl = round(fun.get_value_at(l), digits)
    fr = round(fun.get_value_at(r), digits)
    if fl * fr > 0:
        print("Sorry but Bisection method can not solve an equation with the given interval")
        return None

    while abs(r - l) > constants.EPS:
        m = l + (r - l) / 2
        fm = round(fun.get_value_at(m), digits)
        print(l, r, fl, fr, m, fm, sep=' ')
        if fm * fl > 0:
            l = m
        else:
            r = m
    return (r + l) / 2




# find_root_secant("cos(x) + x**2 - x - 4", -1.56,4)


# print(find_root_newton("x + 4", -3))
