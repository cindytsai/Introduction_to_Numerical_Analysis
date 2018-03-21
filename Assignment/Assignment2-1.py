import numpy as np

def give_me_an_array(n):
    output = np.zeros((10,10), dtype='int64')
    ### START YOUR CODE HERE ###
    output = output + np.fromfunction(lambda i,j: i-j == 1, (10,10))
    output = output + np.fromfunction(lambda i,j: i-j == -1, (10,10))
    output = output + np.fromfunction(lambda i,j: i+j == 8, (10,10))
    output = output + np.fromfunction(lambda i,j: i+j == 10, (10,10))
    output = n * output
    #### END YOUR CODE HERE ####
    return output


