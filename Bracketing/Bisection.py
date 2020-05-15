import Bracketing.constants as constants
from sympy import *
from Bracketing.Function import Function as Func

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


def find_root_secant(function_string, x_prev, x_cur):
    """
    :param x_prev:
    :param x_cur:
    :param function_string: the function given in string format
    :return: the value at which the function is zero (if exists )
    """
    try:
        fun = Func(function_string)
        found = false
        x_prev = round(x_prev, digits)
        x_cur = round(x_cur, digits)
        f_prev = round(fun.get_value_at(x_prev), digits)
        f_cur = round(fun.get_value_at(x_cur), digits)
        for i in range(0, constants.MAX_ITERATIONS):
            r = f_cur * ((x_cur - x_prev) / (f_cur - f_prev))
            x_next = round(x_cur - r, digits)
            # print(x_prev, x_cur, f_prev, f_cur, x_next, sep='   ')

            if abs(r) < constants.EPS:
                found = true
                break

            x_prev = x_cur
            f_prev = f_cur
            x_cur = x_next
            f_cur = round(fun.get_value_at(x_cur), digits)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        return None

    if found == false:
        print("The method diverged , Try using another initial or make sure the function has a root and is continuous")
        return None
    return x_cur


def find_root_newton(function_string, x):
    """
    :param function_string: the equation which we want to get the root
    :param x: the initial guess of the root
    :return: the root of the equation and NONE if the equation diverged or the number of iterations is above MAX_ITERATIONS
    """
    fun = Func(function_string)
    found = false
    for i in range(0, 50):
        fx = round(fun.get_value_at(x), digits)
        gx = round(fun.get_derivative_value_at(x), digits)  # gx is d/dx (fx)
        r = (fx / gx)
        if abs(r) < constants.EPS:
            found = true
            break
        x = round(x - r)

    if found == false:
        print("The method diverged .Sorry but we can not solve this equation using newton ")
        return None
    else:
        return x




# find_root_secant("cos(x) + x**2 - x - 4", -1.56,4)


print(find_root_newton("x + 4", -3))
