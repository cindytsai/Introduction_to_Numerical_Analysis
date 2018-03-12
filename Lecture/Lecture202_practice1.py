import math


def f(x):
    return x - x ** 2 + x ** 3 - x ** 4 + math.sin(x * 13.) / 13.


def fint(x):
    return x ** 2 / 2. - x ** 3 / 3. + x ** 4 / 4. - x ** 5 / 5. - math.cos(x * 13.) / 169.


fint_exact = fint(1.2) - fint(0.)
area, x, h = 0., 0., 1E-3
f0 = f1 = f2 = f(x)
while x < 1.2 - h * 0.5:
    f0, f1, f2 = f2, f(x + h), f(x + h * 2.)
    x += h * 2.
    area += f0 + f1 * 4. + f2
area *= h / 3.

print('Exact: %.16f, Numerical: %.16f, diff: %.16f' % (fint_exact, area, abs(fint_exact - area)))
# ===============================================================================================
area2, x2, h2 = 0., 0., 1E-3
f0 = f1 = f2 = f3 = f(x2)
while x2 < 1.2 - h2 * 0.5:
    f0, f1, f2, f3 = f3, f(x2 + h2), f(x2 + h2 * 2.), f(x2 + h2 * 3.)
    x2 = x2 + h2 * 3.
    area2 = area2 + f0 * 3. + f1 * 9. + f2 * 9. + f3 * 3.
area2 = area2 * h2 / 8.

print('Exact: %.16f, Numerical: %.16f, diff: %.16f' % (fint_exact, area2, abs(fint_exact - area2)))