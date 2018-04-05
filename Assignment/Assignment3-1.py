import numpy as np
import scipy.linalg as linalg

def solve_equations(b):
    output = np.zeros(6)
    ### START YOUR CODE HERE ###
    a = np.array([[1,2,0,0,0,0],
                  [1,2,3,0,0,0],
                  [0,2,3,4,0,0],
                  [0,0,3,4,5,0],
                  [0,0,0,4,5,6],
                  [0,0,0,0,5,6]])
    output = linalg.solve(a, b)
    #### END YOUR CODE HERE ####
    return output

