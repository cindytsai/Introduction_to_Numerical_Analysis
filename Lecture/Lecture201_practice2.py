import math
import decimal

pi = decimal.Decimal('0.')
numerator = decimal.Decimal('1.')

for n in range(100001):
    pi += numerator / (decimal.Decimal('2.') * n + decimal.Decimal('1.')) * decimal.Decimal('4.')
    numerator = -numerator

    if n == 1000 or n == 10000 or n == 100000:
        print('-' * 30)
        print('Sum up to', n, 'step:')
        print('pi(calc) = %.15f' % float(pi))
        print('diff = %.15f' % abs(math.pi - float(pi)))
