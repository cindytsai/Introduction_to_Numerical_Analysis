from scipy import optimize
import math

def asin_func(R):
    asin = optimize.newton(lambda x: math.sin(x) - R, 0)
    return asin
def acos_func(R):
    acos = optimize.newton(lambda x: math.cos(x) - R, 0.3)
    return acos

for i in [0.1, 0.5, 0.9, 1.0]:
    print ("Implementation asin:", asin_func(i))
    print ("Standard       asin:", math.asin(i))
    print ("Implementation acos:", acos_func(i))
    print ("Standard       acos:", math.acos(i))
