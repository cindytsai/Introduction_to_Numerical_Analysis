import numpy as np
from scipy.integrate import solve_ivp

init_data = [[0.362, +0.380, -1.954, -2.364, +0.461],
             [0.168, +0.032, +0.631, +0.233, -0.608],
             [0.413, +0.280, -0.095, -0.672, -0.369],
             [0.209, -1.669, +0.116, -1.965, +0.237],
             [0.172, +0.376, +0.673, -0.370, +0.723],
             [0.322, -0.583, +0.355, -0.405, +0.831],
             [0.289, -0.619, -0.960, -0.525, -1.366],
             [0.108, +0.626, -1.931, +0.276, +1.698],
             [0.491, +0.499, +0.217, -1.237, +0.084],
             [0.325, +0.781, +1.452, -0.295, -0.827]];

def f(t,y):
    dydt = np.zeros(40)
    ### START YOUR CODE HERE ###
    dydt = dydt.reshape(10,4)
    y = y.reshape(10,4)
    vx = y[:,2]
    vy = y[:,3]
    x  = y[:,0]
    y  = y[:,1]
    def Rij(xi,yi,xj,yj):
        return np.sqrt((xi-xj)**2 + (yi-yj)**2)
    def axyi(i):
        axi, ayi = 0, 0
        for j in range(10):
            if j == i:
                continue
            R = Rij(x[i],y[i],x[j],y[j])
            temp = (m[j]/R**2) * (1/R)
            axi = axi + temp * (x[j] - x[i])
            ayi = ayi + temp * (y[j] - y[i])
        return (axi, ayi)
    for i in range(10):
        dydt[i,0], dydt[i,1] = vx[i], vy[i]
        dydt[i,2], dydt[i,3] = axyi(i)
    dydt = dydt.reshape(40)
    #### END YOUR CODE HERE ####
    return dydt

def solve_for_gravity(delta_t):
    positions = np.zeros((10,2))
    ### START YOUR CODE HERE ###
    data = np.asarray(init_data)
    global m
    m = data[:,0]
    y = data[:,1:5]
    y = y.reshape(40)
    t = 0.
    t_step = delta / 100.
    while t < delta_t:
        sol = solve_ivp(f,[t,t+t_step],y)
        y = sol.y[:,-1]
        t = sol.t[-1]
    y = y.reshape(10,4)
    positions = y[:,0:2]
    #### END YOUR CODE HERE ####
    return positions
