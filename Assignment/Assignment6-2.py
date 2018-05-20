import numpy as np

def gen_random_chords(N):
    res = np.zeros(N)
    ### START YOUR CODE HERE ###
    a = 2. * np.pi * np.random.rand(N)
    b = 2. * np.pi * np.random.rand(N)
    ax, ay = np.cos(a), np.sin(a)
    bx, by = np.cos(b), np.sin(b)
    res = np.sqrt((bx-ax)**2 + (by-ay)**2)
    #### END YOUR CODE HERE ####
    return res

