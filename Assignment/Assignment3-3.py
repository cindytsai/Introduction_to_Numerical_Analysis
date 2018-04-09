import numpy as np
import scipy.linalg as linalg

x = np.array([1.00,2.00,3.00,4.00,5.00])

y = np.array([5.23,4.32,3.05,2.76,2.01])

Sig = np.array([[0.62,0.21,0.12,0.04,0.09],
                [0.21,0.78,0.32,0.10,0.12],
                [0.12,0.32,0.69,0.03,0.15],
                [0.04,0.10,0.03,0.95,0.20],
                [0.09,0.12,0.15,0.20,0.83]])

def scan_leastsquares():
    a_best, b_best,chisq_best = 0., 0., 0.
    ### START YOUR CODE HERE ###
    Sig_inv = linalg.inv(Sig)
    chisq = 1000
    def X(a, b):
        para = y - (a * x + b)
        X2 = np.dot(para, Sig_inv)
        X2 = np.dot(X2, para.T)
        return X2
    for a_try in np.linspace(-1,1,11):
        for b_try in np.linspace(-1,1,11):
            if X(a_try, b_try) < chisq :
                a_best, b_best, chisq = a_try, b_try, X(a_try,b_try)
    chisq_best = chisq
    #### END YOUR CODE HERE ####
    return a_best, b_best, chisq_best
