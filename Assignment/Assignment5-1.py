import numpy as np
from scipy.integrate import solve_ivp

def f(t,y):
    m, g = 1., 9.8
    dydt = np.zeros(4)
    ### START YOUR CODE HERE ###
    vx, vy, v2 = y[2], y[3], y[2]**2+y[3]**2
    v = np.sqrt(v2)
    ax = -(vx/v)*((k0 * v2)/m)
    ay = -(vy/v)*((k0 * v2)/m) - g
    dydt[0], dydt[1] = vx, vy
    dydt[2], dydt[3] = ax, ay
    #### END YOUR CODE HERE ####
    return dydt

def flight_distance(theta, v0, k):
    distance = 0.
    ### START YOUR CODE HERE ###
    global k0
    k0 = k
    height = 0.
    t, t_step = 0, 0.001
    vx, vy = v0*np.cos(theta), v0*np.sin(theta)
    y = np.array([0,0,vx,vy])
    while height >= 0:
        sol = solve_ivp(f, [t,t+t_step], y)
        y = sol.y[:,-1]
        t = sol.t[-1]
        distance = y[0]
        height = y[1]
    #### END YOUR CODE HERE ####
    return distance
