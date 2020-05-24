from sympy import *


def convert_num(term):
    is_float = False
    for i in term:
        if i == '.':
            is_float = True
            break
    if is_float:
        return float(term)
    return int(term)


def is_num(num):
    if isinstance(num, complex):
        return True
    if isinstance(num, float):
        return True
    if isinstance(num, int):
        return True
    for i in num:
        if i == '.':
            continue
        if i < '0' or i > '9':
            return False
    return True


def get_prant(str, start):
    term = '('
    open = 1
    start += 1
    while open > 0:
        term += str[start]
        if str[start] == '(':
            open += 1
        elif str[start] == ')':
            open -= 1
        start += 1
        if start == len(str) and open != 0:
            raise Exception('bad input ')
    return term


def add_addential_term(terms):
    size = len(terms)
    if size == 0:
        return
    if is_num(terms[size - 1]):
        terms.append('*')
    pass


operator = {'+', '-', '*', '/'}
basic_operator = {'+', '-'}
high_operator = {'*', '/'}


def add_arth(terms, op):
    size = len(terms)
    if op in {'*', '/'}:
        if size == 0 or terms[size - 1] in operator:
            raise Exception('bad input ')
        else:
            terms.append(op)
            return
    if size == 0:
        if op == '-':
            terms.append(op)
        return
    if terms[size - 1] in high_operator:
        if op == '+':
            return
        elif op == '-':
            terms.append('-')
            return
        else:
            raise Exception('bad input ')
    if terms[size - 1] == '-':
        terms.pop()
        if op == '+':
            terms.append('-')
        else:
            if size == 1 or not is_num(terms[size - 2]):
                return
            terms.append('+')
        return
    if terms[size - 1] == '+':
        terms.pop()
        terms.append(op)
        return
    terms.append(op)
    return


def parse(str):
    terms = []
    n = len(str)
    i = 0
    while i < n:
        if i < n - 5 and str[i:i + 4] in {'tan(', 'exp(', 'sin(', 'cos('}:
            term = str[i:i + 3] + get_prant(str, i + 3)
            i += len(term) - 1
            add_addential_term(terms);
            terms.append(term)
        elif i < n - 4 and str[i:i + 3] == 'ln(':
            term = str[i:i + 2] + get_prant(str, i + 2)
            i += len(term) - 1
            add_addential_term(terms);
            terms.append(term)
        elif str[i] == '(':
            term = get_prant(str, i)
            i += len(term) - 1
            add_addential_term(terms);
            terms.append(term)
        elif str[i] == 'x':
            add_addential_term(terms);
            terms.append('x')
        elif i < n - 1 and str[i:i + 2] == '**':
            terms.append('**')
            i += 1
        elif str[i] in ['*', '/', '+', '-']:
            add_arth(terms, str[i])
        elif is_num(str[i]):
            term = ''
            while i < n and is_num(str[i]):
                term += str[i]
                i += 1
            i -= 1
            terms.append(term)
        elif str[i] != ' ':
            raise Exception('bad input ')
        i += 1
    return terms


def get_coefficient(function_string):
    for char in function_string:
        if char in {'s', 'c', 't', 'e', 'l'}:
            raise ("function isn't polynomial ")
    index = 0
    function_string = str(expand(function_string))
    terms = parse(function_string)
    size = len(terms)
    ans = []
    large = -1
    next_power = -1

    while index < size:
        if terms[index] == '**':
            if terms[index + 1] == '-':
                raise Exception('power is negative')
        index += 1
    index = 0

    while index < size:
        if terms[index] == 'x':
            if index == 0 or terms[index - 1] == '+':
                coff = 1
            elif terms[index - 1] == '-':
                coff = -1
            else:
                num = convert_num(terms[index - 2])
                if index == 2 or terms[index - 3] == '+':
                    coff = num
                else:
                    coff = -1 * num

            if large == -1:
                if index < size - 1 and terms[index + 1] == '**':
                    large = convert_num(terms[index + 2])
                else:
                    large = 1
                next_power = large - 1

            else:
                if index == size - 1 or terms[index + 1] != '**':
                    next = 1
                else:
                    next = convert_num(terms[index + 2])
                temp_next = next
                while next != next_power:
                    ans.append(0)
                    next += 1
                next_power = temp_next - 1

            ans.append(coff)

        index += 1

    if next_power != -1:
        while next_power != 0:
            ans.append(0)
            next_power -= 1

    index = 0
    while index < size:
        if is_num(terms[index]) and (index == size - 1 or terms[index + 1] in {'+', '-'}):
            if index == 0 or terms[index - 1] == '+':
                ans.append(convert_num(terms[index]))
                return ans
            if terms[index - 1] == '-':
                ans.append(-1 * convert_num(terms[index]))
                return ans
        index += 1
    ans.append(0)
    return ans


