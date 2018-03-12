import math
import scipy.integrate as integrate

def f(x):
    return math.cos(x)
def fint(x):
    return math.sin(x)

for i in [math.pi, 100. * math.pi, 1000. * math.pi, 100.5 * math.pi, 1000.5 * math.pi] :
	fint_exact = fint(i) - fint(0.)
	quad,quaderr = integrate.quad(f,0.,i, limit = 5000)
	print('___________________________')
	print('Exact: %.16f' %  fint_exact)
	print('Numerical: %.16f+-%.16f, diff: %.16f' % (quad, quaderr, abs(fint_exact-quad)))