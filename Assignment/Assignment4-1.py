import numpy as np
import scipy.optimize as opt

def func(x):
    value = 0.
    ### START YOUR CODE HERE ###
    value = np.fabs(np.sin(x) / ((x / (2 * np.pi))**x + np.pi / 8.))
    value = value - (x / (2 * np.pi))
    value = value + (x / (2 * np.pi))**2
    value = value - (1./2.)
    #### END YOUR CODE HERE ####
    return value

def find_all_roots():
    output = np.zeros(5)
    ### START YOUR CODE HERE ###
    para = [0,3,3.5,5,8]
    for i in range(5):
        output[i] = opt.newton(func, para[i])
    #### END YOUR CODE HERE ####
    return output
