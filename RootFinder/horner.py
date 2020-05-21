from RootFinder.Utils import constants
from RootFinder.Utils import parsing

class BirgeVieta:
    def cal(self,fun, initial):
        a = parsing.get_coefficient(fun)
        roots = []
        size = len(a)
        for i in range(size - 1):
            b = []
            c = []
            guess = initial
            for j in range(constants.MAX_ITERATIONS):
                b.append(a[0])
                c.append(a[0])
                for k in range(len(a) - 1):
                    b.append(b[k]*guess + a[k+1])
                for k in range(len(a) - 2):
                    c.append(c[k]*guess + b[k+1])
                if abs(b[len(a)-1]) < constants.EPS:
                    break
                guess = guess - b[len(a) - 1] / c[len(a) - 2]
                b.clear()
                c.clear()
            if abs(b[len(a) - 1]) < constants.EPS:
                roots.append(guess)
            else:
                break
            b.pop(len(a)-1)
            a = b.copy()
        return roots


birge = BirgeVieta()
print(birge.cal("x**3-11*x**2+39*x-45", 4.9))