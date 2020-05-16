from cmath import inf, sqrt

import Bracketing.constants as constants
from Bracketing.Function import Function as Func
import Bracketing.parsing as parse

eps = constants.EPS
max_iterations = constants.MAX_ITERATIONS


def is_num(num):
    for i in num:
        if i < '0' or i > '9':
            return False
    return True


def get_g(function_string):
    terms = parse.parse(function_string)
    __g = []
    n = len(terms)
    i = 0
    while i < n:
        if terms[i] == 'x':
            if i == n - 1 or terms[i + 1] in {'+', '-'}:  # x only

                if i == 0 or terms[i - 1] == '+':  # before is +

                    __g.append("-(" + function_string + "-x)")

                elif terms[i - 1] == '-':  # before is -
                    __g.append(function_string + "+x")

                elif terms[i - 1] == '*':  # before is *

                    if is_num(terms[i - 2]):

                        if i - 2 == 0 or terms[i - 3] == '+':

                            __g.append("(" + function_string + " - " + terms[i - 2] + "*x)/-" + terms[i - 2])

                        elif terms[i - 3] == '-':

                            __g.append("(" + function_string + " + " + terms[i - 2] + "*x)/" + terms[i - 2])

            elif (i == 0 or terms[i - 1] in {'+', '-'}) and terms[i + 1] == '*':  # x * number
                if is_num(terms[i + 2]):
                    if i == 0 or terms[i - 1] == '+':

                        __g.append("(" + function_string + " - x*" + terms[i + 2] + ")/-" + terms[i + 2])

                    elif terms[i - 1] == '-':

                        __g.append("(" + function_string + " + x*" + terms[i + 2] + ")/+" + terms[i + 2])

                elif terms[i + 2] == '-' and is_num(terms[i + 3]):

                    if terms[i - 1] == '+':

                        __g.append("(" + function_string + "+x*" + terms[i + 3] + ")/" + terms[i + 3])

                    elif terms[i - 1] == '-':

                        __g.append("(" + function_string + "-x*" + terms[i + 3] + ")/-" + terms[i + 3])

            elif i < n - 2 and terms[i + 1] == '**' and is_num(terms[i + 2]):
                if i == n - 3 or terms[i + 3] in {'+', '-'}:

                    if i == 0 or terms[i - 1] == '+':

                        __g.append("(-(" + function_string + '-x**' + terms[i + 2] + "))**(1/" + terms[i + 2] + ")")

                    elif terms[i - 1] == '-':

                        __g.append("((" + function_string + '+x**' + terms[i + 2] + "))**(1/" + terms[i + 2] + ")")

        i += 1

    __g.append("x-(" + function_string + ")")

    return __g


def find_root_fixed_point(function_string, x):
    __g = get_g(function_string)

    for i in __g:
        root = get_root(i, x)
        if root is not None:
            return root
    return None


def get_root(fun, x):
    print(fun)
    fun = Func(fun)
    iter = 0
    last_value = inf
    while iter < 50 and abs(x - last_value) > constants.EPS and abs(x) < 1000000000000000000:
        iter += 1
        last_value = x
        x = round(fun.get_value_at(x), constants.DIGITS)
    if abs(x - last_value) < constants.EPS:
        print(x)
        return x
    print("sorry we diverge ")
    return None


tt = find_root_fixed_point("3+x*-5", .5)
