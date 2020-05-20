import cmath
def f(x):
    return 5-3*x*9-7*x**3-x**5

xnm2 = 200
xnm1 = 1587
xn = 10000
epsilon = 10 ** -7
i = 0

while abs(f(xn)) > epsilon:
    q = (xn - xnm1) / (xnm1 - xnm2)
    a = q * f(xn) - q * (1 + q) * f(xnm1) + q ** 2 * f(xnm2)
    b = (2 * q + 1) * f(xn) - (1 + q) ** 2 * f(xnm1) + q ** 2 * f(xnm2)
    c = (1 + q) * f(xn)
    # see which x intercept is better
    r = xn - (xn - xnm1) * ((2 * c) / (b + cmath.sqrt(b ** 2 - 4 * a * c)))
    s = xn - (xn - xnm1) * ((2 * c) / (b - cmath.sqrt(b ** 2 - 4 * a * c)))
    if abs(f(r)) < abs(f(s)):
        xplus = r
    else:
        xplus = s
    if xplus.imag == 0j:  # result is real number
        xplus = xplus.real
    xnm2 = xnm1
    xnm1 = xn
    xn = xplus
    i = i + 1
print(i)
print("{:.4f}".format(xplus))
