import numpy as np

def give_me_an_array(n):
    output = np.zeros((n,n), dtype='int64')
    ### START YOUR CODE HERE ###
    output = np.fromfunction(lambda i,j: i+j+1, (n,n))
    #### END YOUR CODE HERE ####
    return output
