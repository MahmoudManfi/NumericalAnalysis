import Bracketing.constants as constants

eps = constants.EPS
max_iterations = constants.MAX_ITERATIONS


def find_root_fixed_point(function_string, x):
    """
    :param function_string: the function  formatted as a string
           You can get the value of the function by importing the  Function module
    :param x: the initial guess you use
    :return: the root of the equation

    *determining the G(x) is your task
    *any assumptions should be stated cleary in comments before the function
     *In case the you could not find the root (the method diverged , we iterated more that max_iterations, you can simply print in
     the console we did not find the root and return None (DON'T THROW ANY EXCEPTION )
    """