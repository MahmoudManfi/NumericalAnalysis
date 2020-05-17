def is_num(di):
    return '0' <= di <= '9'


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
    return term


def parse(str):
    terms = []
    n = len(str)
    i = 0
    while i < n:
        if str[i] in {'t', 'e', 's', 'c'}:
            term = str[i:i + 3]+get_prant(str,i+3)
            i+=len(term)-1
            terms.append(term)
        elif str[i] == 'l':
            term = str[i:i + 2]+get_prant(str,i+2)
            i +=len(term)-1
            terms.append(term)
        elif str[i] == '(':
            term=get_prant(str,i)
            i+=len(term)-1
            terms.append(term)
        elif str[i] == 'x':
            terms.append('x')
        elif str[i:i + 2] == '**':
            terms.append('**')
            i += 1
        elif str[i] in ['*', '/', '+', '-']:
            terms.append(str[i])
        elif is_num(str[i]):
            term = ''
            while i < n and is_num(str[i]):
                term += str[i]
                i += 1
            i -= 1
            terms.append(term)
        i += 1
    return terms
