import Bracketing.constants as constants
from sympy import *
from Bracketing.Function import Function as Func

digits = constants.DIGITS;

def find_root_secant(function_string, x_prev, x_cur):
    """
    :param x_prev:
    :param x_cur:
    :param function_string: the function given in string format
    :return: the value at which the function is zero (if exists )
    """
    try:
        fun = Func(function_string)
        found = False
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

