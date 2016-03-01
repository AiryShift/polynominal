from polynominal import parse_poly


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
    poly = parse_poly(input('Enter a polynominal: '))
    print('You entered a polynominal: {}'.format(poly))
    print('Finding roots to precision of 5 decimal places')

    a = b = 1
    while a and b:
        print('Find a root between...')
        a = input('a: ')
        b = input('b: ')
        print(find_root(poly, a, b))
