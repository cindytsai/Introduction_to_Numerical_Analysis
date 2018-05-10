import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

nbase = 10000
np.random.seed(1234)
vs = np.hstack((np.random.randn(nbase*3)*0.2+3.,np.random.randn(nbase)*0.6+2.8))
vb = np.hstack((np.random.randn(nbase*4)*1.2+2.,np.random.randn(nbase*4)*2.8+1.0))

# uncomment below for displaying the histogram plots
plt.hist(vs, bins=50, color='y', range=(-5.,7.), alpha=0.5)
plt.hist(vb, bins=50, color='g', range=(-5.,7.), alpha=0.5)
plt.show()

def find_the_best_window():
    output = np.zeros(2)
    ### START YOUR CODE HERE ###
    def func_z(p):
        L, U = p[0], p[1]
        Ns = np.sum((vs > L) * (vs < U))
        Nb = np.sum((vb > L) * (vb < U))
        z_inv = -Ns / np.sqrt(Ns + Nb)
        return z_inv
    p_init = np.array([2.2,3.5])
    r = opt.minimize(func_z,p_init,method='Nelder-Mead')
    if r.success:
        output = r.x.round(2)
    #### END YOUR CODE HERE ####
    return output
