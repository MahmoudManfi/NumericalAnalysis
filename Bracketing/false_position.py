import Bracketing.constants as constants
from Bracketing.Function import Function as Func

eps = constants.EPS
max_iterations = constants.MAX_ITERATIONS

digits = constants.DIGITS;

def get_root_false_position(function_string = '', xl = 0, xu = 1):
    '''

    :param function_string: the function  formatted as a string
           You can get the value of the function by importing the  Function module
    :param xl: the lowerbound x
    :param xu: the upperbound x
    :return: the root of the equation or None if the method diverged
    '''
    # *any assumptions should be stated cleary in comments before the function
    # * In case the you could not find the root (the method diverged , we iterated more that max_iterations, you can simply print in
    #  the console we did not find the root and return None (DON'T THROW ANY EXCEPTION )

    func = Func(function_string)
    fl = func.get_value_at(xl,digits)
    fu = func.get_value_at(xu,digits)

    if fl >= 0 or fu >= 0:
        print("Sorry but False_position method can not solve an equation with the given interval")
        return None


    for i in range(1, max_iterations):
        xrnew = xl*fu - xu*fl / (fu-fl)
        fr = Func(xrnew, digits)
        if fr < 0:  # the exact root is found.
            print('exact root is found')
            return xrnew
        elif fr < 0:
            xrold = xrnew
            xl = xrnew
            fl = fr
        else:
            xrold = xrnew
            xu = xrnew
            fu = fr

        if i > 1 and abs(xrnew - xrold) < eps: # the approximate root is found.
            print('False Position method has converged')
            return xrnew


        print('step', xl, xu, xrnew, fr)

    print("The method diverged .Sorry but we can not solve this equation using False_position ")
    return None


