from random import random

from sympy import *
from RootFinder.Bracketing.Bisection import find_root_bisection
from RootFinder.Bracketing.FalsePosition import eps, find_root_falsePosition
from RootFinder.OpenMethods.FixedPoint import find_root_fixedPoint
from RootFinder.OpenMethods.NewtonRaphson import find_root_newtonRaphson
from RootFinder.OpenMethods.Secant import find_root_secant
from RootFinder.OpenMethods.muller import find_root_muller

inf = 1000000


def convert_num(term):
    is_float = False
    for i in term:
        if i == '.':
            is_float = True
            break
    if is_float:
        return float(term)
    return int(term)


def is_poly(terms):
    for term in terms:
        for c in term:
            if c in ['t', 's', 'c', 'e', 'l']:
                return False
    return True


def get_coefficient(terms):
    index = 0
    size = len(terms)
    ans = []
    while index < size:
        if terms[index] == 'x':
            if index == 0 or terms[index - 1] == '+':
                ans.append(1)
            else:
                num = convert_num(terms[index - 1])
                if index == 1 or terms[index - 2] == '+':
                    ans.append(num)
                else:
                    ans.append(num * -1)
        index += 1
    pass


def get_powers(terms):
    index = 0
    size = len(terms)
    ans = []
    while index < size:
        if terms[index] == 'x':
            if index == size - 1 or terms[index + 1] != '**':
                ans.append(1)
            else:
                ans.append(convert_num(terms[index + 2]))
        index += 1
    pass


def try_bisection(functional_string, all=False):
    roots = []
    for i in range(100):
        l = 1 * inf + (random() * (2 * inf))
        r = -1 * inf + (random() * (2 * inf))
        root = find_root_bisection(functional_string, l, r)
        if root is not None:
            if all:
                roots.append(root)
            else:
                return root

    for i in range(1, 100):
        l = 1 * i
        r = -1 * i
        root = find_root_bisection(functional_string, l, r)
        if root is not None:
            if all:
                roots.append(root)
            else:
                return root
    if not all:
        return None
    return roots


def try_false_postion(functional_string, all=False):
    roots = []
    for i in range(100):
        l = -1 * inf + (random() * (2 * inf))
        r = -1 * inf + (random() * (2 * inf))
        root = find_root_falsePosition(functional_string, l, r)
        if root is not None:
            if all:
                roots.append(root)
            else:
                return root
    for i in range(1, 100):
        l = 1 * i
        r = -1 * i
        root = find_root_falsePosition(functional_string, l, r)
        if root is not None:
            if all:
                roots.append(root)
            else:
                return root

    if not all:
        return None
    return roots


def try_fixed_point(functional_string, all=False):
    roots = []
    for i in range(100):
        t = -1 * inf + (random() * (2 * inf))
        root = find_root_fixedPoint(functional_string, t)
        if root is not None:
            if all:
                roots.append(root)
            else:
                return root
    for i in range(1, 100):
        t = i
        root = find_root_fixedPoint(functional_string, t)
        if root is not None:
            if all:
                roots.append(root)
            else:
                return root
        t = -1 * i
        root = find_root_fixedPoint(functional_string, t)
        if root is not None:
            if all:
                roots.append(root)
            else:
                return root

    if not all:
        return None
    return roots


def try_secent(functional_string, all=False):
    roots = []
    for i in range(100):
        l = -1 * inf + (random() * (2 * inf))
        r = -1 * inf + (random() * (2 * inf))
        root = find_root_secant(functional_string, l, r)
        if root is not None:
            if all:
                roots.append(root)
            else:
                return root
    for i in range(1, 100):
        l = 1 * i
        r = -1 * i
        root = find_root_secant(functional_string, l, r)
        if root is not None:
            if all:
                roots.append(root)
            else:
                return root

    if not all:
        return None
    return roots


def try_newton(functional_string,all=False):
    roots = []
    for i in range(100):
        t = -1 * inf + (random() * (2 * inf))
        root = find_root_newtonRaphson(functional_string, t)
        if root is not None:
            if all:
                roots.append(root)
            else:
                return root
    for i in range(1, 100):
        try:
            root = find_root_newtonRaphson(functional_string, i)
            if root is not None:
                if all:
                    roots.append(root)
                else:
                    return root
            root = find_root_newtonRaphson(functional_string, i)
            if root is not None:
                if all:
                    roots.append(root)
                else:
                    return root
        except:
            continue

    if not all:
        return None
    return roots


def try_muller(functional_string, all=False):
    roots = []
    for i in range(100):
        a = -1 * inf + (random() * (2 * inf))
        b = -1 * inf + (random() * (2 * inf))
        c = -1 * inf + (random() * (2 * inf))
        try:
            root = find_root_muller(functional_string, a, b, c)
            if not all:
                return root
            roots.append(root)
        except:
             continue;
    return roots


def merge(ans, root):
    if type(root) == float or type(root) == int:
        ans.append(root)
        return ans
    if type(root) == complex:
        if root.imag < eps:
            ans.append(root.real)
            return ans
        ans.append(root)
        ans.append(root.conjugate())
        return ans


def get_one_root(functional_string):
    if functional_string == "":
        return None

    root = try_bisection(functional_string)
    if root is not None:
        return root

    root = try_false_postion(functional_string)
    if root is not None:
        return root

    root = try_fixed_point(functional_string)
    if root is not None:
        return root

    root = try_secent(functional_string)
    if root is not None:
        return root

    root = try_newton(functional_string)
    if root is not None:
        return root

    # return try_muller(functional_string)


def divide_root(functional_string, root):
    terms = parsing.parse(functional_string)
    if type(root)==complex :
        if root.imag<eps:
           root=root.real
        else:

    coefficient = get_coefficient(terms)
    powers = get_powers(terms)

    pass


def solve_poly(functional_string):
    if functional_string == "":
        return []

    root = get_one_root(functional_string)
    if root is not None:
        return merge(solve_poly(divide_root(functional_string, root)), root)


def get_poly_terms(function_string):
    index = 0
    size = len(function_string)
    while index < size:
        if function_string[index] in {'t', 's', 'c', 'l'}:
            break
        else:
            index += 1
    while index >= 0 and function_string[index] not in {'+', '_'}:
        index -= 1
    index -= 1
    if index <= 0:
        return ""
    return function_string[0:index]


def remove_dublicats(roots):
    real_roots = []
    image_roots = []
    for root in roots:
        if root is not None:
            if type(root)==complex:
                if root.imag<eps:
                    real_roots.append(root.real)
                else:
                    image_roots.append(root)
            else:
                real_roots.append(root)
    ans_real=[]
    for real in real_roots:
        add=true
        for prev in ans_real:
            if abs(real-prev)<eps:
                add=False
                break
        if add:
            ans_real.append(real)

    ans_imagine=[]
    for imagine in image_roots:
        add = true
        for prev in ans_imagine:
            if abs(imagine.real - prev.real) < eps and abs(imagine.imag - prev.imag):
                add = False
                break
        if add:
            ans_imagine.append(imagine)

    return [ans_real , ans_imagine]


def solve_non_poly(function_string, initial_guess):
    roots = []
    for guess in initial_guess:
        roots.append(find_root_newtonRaphson(function_string, guess))
        roots.append(find_root_fixedPoint(function_string, guess))

    roots.append(try_bisection(function_string, true))
    roots.append(try_false_postion(function_string, true))
    roots.append(try_fixed_point(function_string, true))
    roots.append(try_secent(function_string, true))
    roots.append(try_newton(function_string, true))
    roots.append(try_muller(function_string, true))
    return remove_dublicats(roots)


def solve(function_string):
    function_string = simplify(function_string)
    if is_poly(function_string):
        return solve_poly(function_string)

    initial_guess = solve_poly(get_poly_terms(function_string))
    return solve_non_poly(initial_guess)

p=get_one_root("x**2+x*2-100")
print(p)