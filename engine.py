from math import floor, sqrt

from RootFinder.Utils.parsing import parse, is_num


def is_poly_term(term):
    if term[0] in ['t', 's', 'c', 'e', 'l']:
        return False
    if term[0] == '(':
        return is_poly_term(term[1:len(term) - 1])
    return True


def get_poly(terms):
    poly_terms = []
    size = len(terms)
    index = 0
    while index < size:
        if is_poly_term(terms[index]):
            poly_terms.append(terms[index])
            index += 1
        else:
            index += 1
            size_poly = len(poly_terms)
            while size_poly > 0 and terms[size_poly - 1] not in {'+', '-'}:
                size_poly -= 1
                poly_terms.pop()
            if size_poly != 0:
                poly_terms.pop()
            while terms[index + 1] not in {'+', '-'}:
                index += 1
    return poly_terms


def convert_num(term):
    is_float = False
    for i in term:
        if i == '.':
            is_float = True
            break
    if is_float:
        return float(term)
    return int(term)


def get_coff(coff):
    if coff == 'x':
        return 1;
    if is_num(coff):
        return convert_num(coff)
    raise Exception('bad input ')

    pass


def get_div(num):
    limit = floor(sqrt(num))
    div = []
    for i in range(1, limit + 1):
        if num % i == 0:
            div.append(i)
            if i != num / i:
                div.append(num / i)

    return div


def get_initial_guess_fac(polynomial):
    size = len(polynomial)
    first_coff = get_coff(polynomial[0])
    constant = get_coff(polynomial[size - 1])
    div1 = get_div(first_coff)
    div2 = get_div(constant)
    initial_guess = []
    for it1 in div1:
        for it2 in div2:
            initial_guess.append(it2 / it1)
    return initial_guess


def get_real_root_isolation_guess(polynomial):
    
    pass


def solve_poly(polynomial):
    initial_guess = get_initial_guess_fac(polynomial)
    initial_guess.append(get_real_root_isolation_guess(polynomial))
    solve_poly(polynomial, initial_guess)

    pass


def solve(function_string):
    terms = parse(function_string)
    polynomial = get_poly(terms)
    poly_roots = solve_poly(polynomial)
    real_roots = get_real_roots(poly_roots)
    imagine_roots = get_imagine_roots(poly_roots)
    roots = __solve(function_string, real_roots)
    return roots
