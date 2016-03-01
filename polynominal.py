import re

POSITIVE = True
NEGATIVE = False


class Term():
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power

    def evaluate(self, value):
        return value**self.power * self.coefficient

    def __str__(self):
        return '{}x{}'.format(self.coefficient, self.power)

    def __repr__(self):
        return 'Term({})'.format(self.__str__())


class Polynominal():
    def __init__(self, *terms):
        self.terms = terms

    def evaluate(self, value):
        result = 0
        for term in self.terms:
            result += term.evaluate(value)
        return result

    def __str__(self):
        return ' '.join(str(i) for i in self.terms)

    def __repr__(self):
        return 'Polynominal({})'.format(self.__str__())


def parse_term(term, sign):
    if 'x' in term:
        term = term.split('x')
    else:
        term = [term]

    coefficient = 1
    if term[0] != '':
        coefficient = float(term[0])

    power = 1
    if len(term) == 2 and term[1] != '':
        power = int(term[1])
    elif len(term) == 1:
        power = 0

    if sign == NEGATIVE:
        coefficient *= -1
    return Term(coefficient, power)


def parse_poly(poly):
    poly = re.split(r'([-\+])', poly)
    poly = [i.strip() for i in poly]
    processed = []

    # process first term by itself
    first_term = poly[0]
    if first_term[0] == '-':
        first_term = parse_term(first_term[:1], NEGATIVE)
    else:
        first_term = parse_term(first_term, POSITIVE)
    processed.append(first_term)

    # process the remainder
    for i in range(1, len(poly), 2):
        sign = POSITIVE if poly[i] == '+' else NEGATIVE
        term = poly[i + 1]
        processed.append(parse_term(term, sign))
    return Polynominal(*processed)


def same_sign(a, b):
    return a > 0 and b > 0 or not a > 0 and not b > 0


def find_root(poly, a, b):
    if not a or not b:
        return ''
    a, b = float(a), float(b)
    if same_sign(poly.evaluate(a), poly.evaluate(b)):
        return 'No confirmed root between {} and {}'.format(a, b)

    while round(a, 5) != round(b, 5):
        y_a, y_b = poly.evaluate(a), poly.evaluate(b)
        middle = (a + b) / 2
        y_middle = poly.evaluate(middle)
        if y_a == 0:
            return a
        elif y_b == 0:
            return b
        elif y_middle == 0:
            return middle

        if same_sign(y_middle, y_a):
            a = middle
        else:
            b = middle

    return round(a, 5)


if __name__ == '__main__':
    print(parse_poly(input('Enter a polynominal: ')))
