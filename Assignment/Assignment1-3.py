import math
import scipy.integrate as integrate


def convoluted_BreitWigner(E, M, Gamma, sigma):
    value = 0.
    ### START YOUR CODE HERE ###

    def func(x):
        para = ((E - x)**2 - M**2)**2 + (M * Gamma)**2
        f = (1. / para) * math.exp(-x**2 / (2. * sigma**2))
        return f

    (value, error) = integrate.quad(func, -sigma * 3., sigma * 3.)

    #### END YOUR CODE HERE ####

    return value
