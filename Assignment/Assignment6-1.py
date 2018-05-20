import numpy as np

def gen_random_dist(N, a, b):
    res = np.zeros(N)
    ### START YOUR CODE HERE ###
    r = np.random.rand(N)
    res = ((1+b)**r / (1+a)**(r-1)) - 1    
    #### END YOUR CODE HERE ####
    return res
