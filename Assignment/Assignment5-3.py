import numpy as np
from scipy.integrate import solve_ivp

def f(t,y):
    q, m = 1., 1.
    dydt = np.zeros(6)
    ### START YOUR CODE HERE ###
    x_vector, v_vector = y[0:3], y[3:6]
    dydt[0:3] = v_vector
    dydt[3:6] = (q/m) * (E_vector + np.cross(v_vector, B_vector))
    #### END YOUR CODE HERE ####
    return dydt

def find_tracking_records(B, E):
    Bx,By,Bz = B[0],B[1],B[2]
    Ex,Ey,Ez = E[0],E[1],E[2]
    positions = np.zeros((10,3))
    ### START YOUR CODE HERE ###
    global B_vector, E_vector
    B_vector = np.array([Bx, By, Bz])
    E_vector = np.array([Ex, Ey, Ez])

    index = 1
    y = np.zeros(6)
    t = 0.
    t_step = 0.01
    while t < 10 :
        sol = solve_ivp(f, [t,t+t_step], y)
        y = sol.y[:,-1]
        t = sol.t[-1]
        if t + t_step >= index:
            positions[index-1,:] = y[0:3]
            index = index + 1
    #### END YOUR CODE HERE ####
    return positions
