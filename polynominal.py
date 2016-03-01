import re

POSITIVE = True
NEGATIVE = False


class Term():
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power

    def evaluate(self, value):
        return value**self.power * self.coefficient


class Polynominal():
    def __init__(self, *terms):
        self.terms = terms

    def evaluate(self, value):
        result = 0
        for term in self.terms:
            result += term.evaluate(value)
        return result


def parse_term(term, sign):
    if 'x' in term:
        term = term.split('x')
    else:
        term = [term]
    coefficient = int(term[0])
    power = 0
    if len(term) == 2:
        power = int(term[1])



def parse_poly(poly):
    """
    Format:
    """
    poly = re.split(r'([-\+])', poly)
    return poly


if __name__ == '__main__':
    print(parse_poly(input('Enter a polynominal: ')))
