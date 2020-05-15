import Bracketing.constants as constants

eps = constants.EPS
max_iterations = constants.MAX_ITERATIONS


def get_root_false_position(function_string, left, right):
    """

    :param function_string: the function  formatted as a string
           You can get the value of the function by importing the  Function module
    :param left: the lowerbound x
    :param right: the upperbound x
    :return: the root of the equation
    *any assumptions should be stated cleary in comments before the function
    * In case the you could not find the root (the method diverged , we iterated more that max_iterations, you can simply print in
     the console we did not find the root and return None (DON'T THROW ANY EXCEPTION )
    """
