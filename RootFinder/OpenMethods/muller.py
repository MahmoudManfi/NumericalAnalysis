import cmath

from RootFinder.Bracketing.FalsePosition import eps
from RootFinder.Utils.eval_success import eval_success


def find_root_muller(function_string):

    xnm2 = 2
    xnm1 = 5
    xn = 10
    while abs(eval_success(function_string,xn)) >eps :
        f_xn=eval_success(function_string,xn)
        f_xnm1=eval_success(function_string,xnm1)
        f_xnm2=eval_success(function_string,xnm2)
        q = (xn - xnm1) / (xnm1 - xnm2)
        a = q * f_xn - q * (1 + q) * f_xnm1 + q ** 2 * f_xnm2
        b = (2 * q + 1) * f_xn - (1 + q) ** 2 * f_xnm1 + q ** 2 * f_xnm2
        c = (1 + q) * f_xn
        r = xn - (xn - xnm1) * ((2 * c) / (b + cmath.sqrt(b ** 2 - 4 * a * c)))
        s = xn - (xn - xnm1) * ((2 * c) / (b - cmath.sqrt(b ** 2 - 4 * a * c)))
        if abs(eval_success(function_string,r)) < abs(eval_success(function_string,s)):
            xplus = r
        else:
            xplus = s
        if hasattr(xplus, 'imag') and  xplus.imag == 0j:
            xplus = xplus.real
        xnm2 = xnm1
        xnm1 = xn
        xn = xplus
        i = i + 1
    return xplus
