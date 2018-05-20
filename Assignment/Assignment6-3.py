import numpy as np

def gen_smeared_exp(N):
    res = np.zeros(N)
    ### START YOUR CODE HERE ###
    rx = np.random.rand(N)
    x = -1.6 * np.log(1 - rx)
    ry1 = np.random.rand(N)
    ry2 = np.random.rand(N)
    Y = np.sqrt(-2.*np.log(ry1)) * np.sin(2.*np.pi*ry2)
    res = 0.2 * Y + x
    #### END YOUR CODE HERE ####
    return res
