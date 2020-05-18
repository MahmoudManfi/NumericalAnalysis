def is_num(num):
    if (isinstance(num, complex)):
        return True
    if (isinstance(num, float)):
        return True
    if (isinstance(num, int)):
        return True
    for i in num:
        if i < '0' or i > '9':
            return False
    return True


def get_prant(str, start):
    term = '(';
    open = 1
    start += 1;
    while open > 0:
        term += str[start]
        if str[start] == '(':
            open += 1
        elif str[start] == ')':
            open -= 1
        start += 1
        if start==len(str) and open!=0:
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
        if op=='+':
            return
        elif op=='-':
            terms.append('-')
            return
        else:
          raise Exception('bad input ')
    if terms[size - 1] == '-':
        terms.pop()
        if op == '+':
            terms.append('-')
        else:
            if size==1 or not is_num(terms[size-2]) :
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
        elif str[i]!=' ':
            raise Exception('bad input ')
        i+=1
    return terms


