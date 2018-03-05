import math
import decimal

nsides = 6
length = decimal.Decimal('1.')

for i in range(20):
    length = (decimal.Decimal('2.') - (decimal.Decimal('4.') - length ** 2) ** decimal.Decimal('0.5')) ** decimal.Decimal('0.5')
    nsides *= 2
    pi = length * nsides / decimal.Decimal('2.')

    print('-'*30)
    print('Polygon of',nsides,'slides:')
    print('pi(calc) = %.15f' % float(pi))
    print('diff = %.15f' % abs(math.pi-float(pi)))
