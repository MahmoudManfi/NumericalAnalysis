from RootFinder.Utils.Function import Function as Func

from RootFinder.Utils import constants

digits = constants.DIGITS;


def find_root_newtonRaphson(function_string, x = 0):
    """
    :param function_string: the equation which we want to get the root
    :param x: the initial guess of the root
    :return: the root of the equation and NONE if the equation diverged or the number of iterations is above MAX_ITERATIONS
    """
    fun = Func(function_string)
    found = False
    for i in range(0, 50):
        fx = round(fun.get_value_at(x), digits)
        gx = round(fun.get_derivative_value_at(x), digits)  # gx is d/dx (fx)
        r = (fx / gx)
        if abs(r) < constants.EPS:
            found = True
            break
        x = round(x - r)

    if found == False:
        print("The method diverged .Sorry but we can not solve this equation using newton ")
        return None
    else:
        return x

