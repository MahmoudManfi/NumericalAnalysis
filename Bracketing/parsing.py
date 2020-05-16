def is_num(di):
    return '0' <= di <= '9'


def parse(str ):

        terms = []
        signs = []
        n = len(str)
        i = 0
        while i < n:
            if str[i] in {'t', 'e', 's', 'c'}:
                term = str[i:i + 4]
                i += 4
                open = 1
                while open > 0:
                    term += str[i]
                    if str[i] == '(':
                        open += 1
                    elif str[i] == ')':
                        open -= 1
                    i += 1
                terms.append(term)
                i -= 1
            elif str[i] == '(':
                open = 1
                i += 1
                term = "("
                while open > 0:
                    term += str[i]
                    if str[i] == '(':
                        open += 1
                    elif str[i] == ')':
                        open -= 1
                    i += 1
                i -= 1
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
                while i<n and is_num(str[i]):
                    term += str[i]
                    i += 1
                i -= 1
                terms.append(term)
            i += 1
        return terms
