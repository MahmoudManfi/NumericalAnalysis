from cmath import sin, cos, tan, exp

from mpmath import ln


import RootFinder.Utils.parsing as Parsing


def is_num(num):
    if isinstance(num, complex):
        return True
    if isinstance(num, float):
        return True
    if isinstance(num, int):
        return True
    for i in num:
        if i < '0' or i > '9':
            return False
    return True


def eval_triangle(term, value):
    contect = term[4:len(term) - 1]
    if term[0:3] == 'sin':
        return sin(eval_success(contect, value))
    if term[0:3] == 'cos':
        return cos(eval_success(contect, value))
    if term[0:3] == 'tan':
        return tan(eval_success(contect, value))
    return None


def is_triangle(term):
    return term[0] in {'s', 'c', 't'}


def is_exp(term):
    return term[0:4] == 'exp('


def eval_exp(term, value):
    contect = term[4:len(term) - 1]
    return exp(eval_success(contect, value))


def is_ln(term):
    return term[0:3] == 'ln('


def eval_ln(term, value):
    connect = term[3:len(term) - 1]
    return ln(eval_success(connect, value))


def is_prant(term):
    return term[0] == '(' and term[len(term) - 1] == ')'


def eval_power(base, power):
    return base ** power


def eval_mul(left, right):
    return left * right


def eval_div(left, right):
    return left / right


def eval_add(left, right):
    return left + right


def eval_sub(left, right):
    return left - right


def eval_success(function_string, value):
    terms = Parsing.parse(function_string)
    if len(terms) == 1 and terms[0] == 'x':
        return value

    index = 0
    size = len(terms)
    while index < size:
        term = terms[index]
        if is_triangle(term):
            terms[index] = eval_triangle(term, value)
        elif is_exp(term):
            terms[index] = eval_exp(term, value)
        elif is_ln(term):
            terms[index] = eval_ln(term, value)
        elif is_prant(term):
            terms[index] = eval_success(term[1:len(term) - 1], value)
        index += 1
        size = len(terms)

    index = 0
    while index < size:
        term = terms[index]
        if term == 'x':
            terms[index] = value
        elif hasattr(term, 'isdigit') and term.isdigit():
            terms[index] = float(term)
            if terms[index].is_integer():
                terms[index] = int(term)

        index += 1

    index = 0
    size = len(terms)
    while index < size:
        term = terms[index]
        if term == '**':
            if terms[index + 1] == '-':
                terms[index - 1:index + 3] = [eval_power(terms[index - 1], -1 * terms[index + 2])]
            else:
                terms[index - 1:index + 2] = [eval_power(terms[index - 1], terms[index + 1])]
            size = len(terms)
        else:
            index += 1

    index = 0

    while index < size:
        term = terms[index]
        if term == '*':
            if terms[index + 1] == '-':
                terms[index - 1:index + 3] = [eval_mul(terms[index - 1], -1 * terms[index + 2])]
            else:
                terms[index - 1:index + 2] = [eval_mul(terms[index - 1], terms[index + 1])]
            size = len(terms)


        elif term == '/':
            if terms[index + 1] == '-':
                terms[index - 1:index + 3] = [eval_div(terms[index - 1], -1 * terms[index + 2])]
            else:
                terms[index - 1:index + 2] = [eval_div(terms[index - 1], terms[index + 1])]
            size = len(terms)
        else:
            index += 1

    index = 0
    while index < size:
        term = terms[index]
        if term == '+':
            terms[index - 1:index + 2] = [eval_add(terms[index - 1], terms[index + 1])]
            size = len(terms)

        elif term == '-':
            if index == 0 or not is_num(terms[index - 1]):
                terms[index:index + 2] = [eval_sub(0, terms[index + 1])]
            else:
                terms[index - 1:index + 2] = [eval_sub(terms[index - 1], terms[index + 1])]
            size = len(terms)

        else:
            index += 1

    if len(terms) != 1:
        raise Exception('bad input ')

    return terms[0]


# eval_success("tan(5*x+8)**6+x*2+5",1)
# print(eval_success("x*-3*-+-+--10", 7))
# print(eval_success("x+-x+-x+-x*p", 7))
# print(eval_success("x+-x+-x+-x*x", 7))
# print(eval_success("2tan(2x)/", 7))
