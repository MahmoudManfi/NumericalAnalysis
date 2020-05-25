import RootFinder.Utils.constants as constants
from RootFinder.Utils.Function import Function as Func
from RootFinder.Utils.Formatter import Formatter as Formatter
eps = constants.EPS


def find_root_falsePosition(function_string , xl, xu):

    '''
    :param function_string: the function  formatted as a string
           You can get the value of the function by importing the  Function module
    :param xl: the lowerbound x
    :param xu: the upperbound x
    :return: the root of the equation or None if the method diverged
    '''
    formatter = Formatter()
    formatter.add_entry("Xl", "Xu", "F(Xl)", "F(Xu)", "Xr","F(Xr)")
    func = Func(function_string)
    fl = func.get_value_at((xl))
    fu = func.get_value_at((xu))

    # if ((fl < 0 and fu<0) or ((fu > 0) and (fl> 0))):
    if fl * fu > 0:
        print("Sorry but False_position method can not solve an equation with the given interval")
        return None

    for i in range(0, constants.MAX_ITERATIONS):
        xrnew = (xl*fu - xu*fl) / (fu-fl)
        fr = func.get_value_at(xrnew)
        formatter.add_entry(xl, fl, xu, fu, xrnew, fr)
        if fr == 0:  # the exact root is found.
            print('exact root is found using false position ')
            formatter.display_steps()
            return xrnew
        elif fr * fl >  0 :
            xl = xrnew
            fl = fr
        else:
            xu = xrnew
            fu = fr

        if (i > 0) and (abs(xrnew - xrold) < eps):
            print('False Position method has converged ')
            formatter.display_steps()
            return xrnew

        xrold = xrnew

    print("The method diverged .Sorry but we can not solve this equation using False_position ")
    return None


#print(find_root_falsePosition("2*x**3 - 1" , -1 , 2))
# get_root_false_position()