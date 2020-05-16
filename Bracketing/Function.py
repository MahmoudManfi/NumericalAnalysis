from sympy import *
from sympy.parsing.sympy_parser import *
from Bracketing.parsing import parse

class Function:
    def __init__(self, function):
        """the function is a valid string representing the function  """
        """the function is assumed to be a function of x """

        transformation = standard_transformations + (implicit_application,)
        # self.f = parse_expr(function, transformations=transformation, )
        self.f = parse(function)
        for i in self.f:
            print(i)
        self.__x = symbols('x')

    def get_value_at(self, x):
        """ get the value of the function at x """
        ans = self.f.subs(self.__x, x)
        return ans.evalf()

    def get_derivative_value_at(self, x):
        derivative = self.f.diff(self.__x)
        ans = derivative.subs(self.__x, x)
        return ans

