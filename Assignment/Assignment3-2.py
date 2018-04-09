import numpy as np
import scipy.linalg as linalg

def cov_to_corr(cov):
    output = np.zeros(cov.shape)
    ### START YOUR CODE HERE ###
    diag = np.diag(cov)
    diag = np.sqrt(diag)
    output = cov / diag
    output = output / diag[:,None]
    #### END YOUR CODE HERE ####
    return output
