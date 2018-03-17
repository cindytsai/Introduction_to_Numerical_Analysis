import math
import scipy.integrate as integrate


def func(x):
    value = 0.
    ### START YOUR CODE HERE ###
    for n in range(1, 6):
        p = n * math.pi * x
        value = value + (1 + (math.sin(p) * x) + (math.cos(p) * x**2))
    #### END YOUR CODE HERE ####
    return value


def func_integrated(x):
    value = 0.
    ### START YOUR CODE HERE ###
    (value, error) = integrate.quad(func, -x, x)
    #### END YOUR CODE HERE ####
    return value
