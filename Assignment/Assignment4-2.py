import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

xmin, xmax, xbinwidth = 0.,2.,0.05
vx = np.linspace(0.,2.,41)
vy = np.array([+0.3802, +0.8620, +1.0819, +1.2007, +1.3590, +0.8477, +1.1862, +0.5973,
               +0.1126, -0.2399, -0.3754, -0.3172, -0.2139, -0.1561, +0.1690, +0.4099,
               +0.4267, +0.6841, +1.2772, +1.1771, +1.6481, +0.9490, +0.4869, +0.5355,
               +0.2388, -0.1428, -0.4039, -0.5386, -0.3652, +0.0908, +0.2229, +0.4515,
               +0.7118, +1.0343, +0.8454, +1.1228, +1.3083, +0.8966, +0.6850, +0.2714,
               +0.0741])
vyerr = np.array([+0.2097, +0.0996, +0.1363, +0.1744, +0.1246, +0.2046, +0.1963, +0.1444,
                  +0.1506, +0.1648, +0.1455, +0.1655, +0.1405, +0.1350, +0.1537, +0.1338,
                  +0.1364, +0.1834, +0.1136, +0.0805, +0.2492, +0.1433, +0.1538, +0.1510,
                  +0.1299, +0.1121, +0.0890, +0.1720, +0.1791, +0.2193, +0.1572, +0.1482,
                  +0.1290, +0.1922, +0.1405, +0.1165, +0.1712, +0.0951, +0.2398, +0.1670,
                  +0.1479,])

# uncomment below for displaying the data points
#plt.errorbar(vx, vy, vyerr, c='blue', fmt = 'o')
#plt.show()

def model(x, n, k, phi, bias):
    value = 0.
    ### START YOUR CODE HERE ###
    value = n * np.sin(k * x + phi) + bias
    #### END YOUR CODE HERE ####
    return value

def find_the_parameters():
    output = np.zeros(4)
    ### START YOUR CODE HERE ###
    def fcn(p):
        expt = model(vx, p[0], p[1], p[2], p[3])
        delta = (vy - expt) / vyerr
        return (delta ** 2).sum()
    p_init = np.array([0.5,8,0,0.5])
    r = opt.minimize(fcn,p_init)
    output = r.x
    #### END YOUR CODE HERE ####
    return output
