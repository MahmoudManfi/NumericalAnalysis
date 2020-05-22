from RootFinder.Utils.Function import Function

# check the validation of inputs
def check(x, fx, n):
    matrix = [x.copy(), fx.copy()]  # to save the order of x and fx
    x.sort()
    fx.sort()
    size_x = len(x)
    size_fx = len(fx)
    if size_x != size_fx or size_x < 2 or n > size_x-1:
        return False
    for i in range(size_x-1):
        if x[i] == x[i+1] : # or fx[i] == fx[i+1]:
            return False
    for i in range(size_x):
        index = matrix[0].index(x[i],0,size_x)
        fx[i] = matrix[1][index]
    return True

# put (x - value) this format in string
def build_parentheses(x):
    container = []
    for i in range(len(x)):
        if x[i] == 0:
            container.append('*x')
        else:
            container.append('*(x - ' + str(x[i]) + ')')
    return container


# put the number in form of string where there is space between it and its sign
def sign_string(number):
    res = ''
    if number > 0:
        res += ' + '
    else:
        res += ' - '
    res += str(abs(number))
    return res


class Newton:
    # return array b which the coefficient of our function
    def cal(self, x, fx):
        size = len(x)
        b = [fx[0]]
        for i in range(1, size):
            top = 0; temp = []
            for j in range(len(fx)-1):
                temp.append((fx[j+1] - fx[j])/(x[j+i]-x[top]))
                top += 1
            fx = temp
            b.append(fx[0])
        return b

    # calculate the query that required from the user
    # before you send the query you should check that the query not equal any value of values of x in our list
    def get_value(self, x, b, query):
        value = 0
        for i in range(len(x)-1,0,-1):
            value += b[i]
            value *= (query - x[i-1])
        value += b[0]
        return value

    # return string the equation
    def get_equ(self, x, b):
        res = ''
        size = len(x)
        container = build_parentheses(x)
        for i in range(size):
            if b[i] == 0:
                continue
            if len(res) == 0:
                res += str(b[i])
            else:
                res += sign_string(b[i])
            for j in range(i):
                res += container[j]
        return res


class Lagrange:
    def cal(self, x, fx):
        b = fx.copy()
        size = len(x)
        for i in range(size):
            mul = 1
            for j in range(size):
                if i == j:
                    continue
                mul *= (x[i] - x[j])
            b[i] /= mul
        return b

    def get_value(self, x, b, query):
        mul = 1
        size = len(x)
        for i in range(size):
            mul *= (query - x[i])
        value = 0
        for i in range(size):
            value += (b[i] * (mul/(query - x[i])))
        return value

    def get_equ(self, x, b):
        container = build_parentheses(x)
        size = len(x)
        res = ''
        for i in range(size):
            if b[i] == 0:
                continue
            if len(res) == 0:
                res += str(b[i])
            else:
                res += sign_string(b[i])
            for j in range(size):
                if i == j:
                    continue
                res += container[j]
        return res


# x = [1,2,3,4,5]
# fx = [10, 20, 30, 40, 50]
# check(x, fx, 4)
# newton = Newton()
# b = newton.cal(x, fx)
# eqn = newton.get_equ(x,b)
# print(eqn)
# eqn = eqn.replace('*','')
# # f = Function(eqn)
# print(eqn)