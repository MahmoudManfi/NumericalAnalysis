from RootFinder.Utils.Function import Function as Func

from RootFinder.Utils import constants
from RootFinder.Utils.Formatter import Formatter as Formatter


def find_root_newtonRaphson(function_string, x):
    """
    :param function_string: the equation which we want to get the root
    :param x: the initial guess of the root
    :return: the root of the equation and NONE if the equation diverged or the number of iterations is above MAX_ITERATIONS
    """
    formatter = Formatter()
    formatter.add_entry("Xi", "f(Xi)", "F'(Xi)", "Xi+1")
    fun = Func(function_string)
    found = False
    for i in range(0, constants.MAX_ITERATIONS):
        fx = (fun.get_value_at(x))
        gx = (fun.get_derivative_value_at(x))  # gx is d/dx (fx)
        formatter.add_entry(x , fx , gx , x-fx/gx)
        # print(x , fx , gx , x-x-fx/gx,sep = "<><><><><>")
        r = (fx / gx)
        if abs(r) < constants.EPS:
            found = True
            break
        x = x - r

    if not found:
        print("The method diverged .Sorry but we can not solve this equation using newton ")
        return None
    else:
        formatter.display_steps()
        return x


pp = find_root_newtonRaphson("exp(x) - 4 ", 2)
print(pp)
# print(find_root_newtonRaphson("x**2 - 4" , 0.25))
