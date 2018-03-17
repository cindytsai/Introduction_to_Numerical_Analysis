import math
import scipy.misc as misc


def func(x):
    value = 1.
    ### START YOUR CODE HERE ###
    for n in range(1, 5):
        p = (n * math.pi * x) / 2.
        value = value * ((math.cos(p) * math.cosh(x)) + (math.sin(p) * math.sinh(x)))
    #### END YOUR CODE HERE ####
    return value


def func_first_derivative(x):
    value = 1.
    ### START YOUR CODE HERE ###
    value = misc.derivative(func, x, dx=10**-5)
    #### END YOUR CODE HERE ####
    return value