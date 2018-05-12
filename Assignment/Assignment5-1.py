import numpy as np
from scipy.integrate import solve_ivp

def f(t,y):
    m, g = 1., 9.8
    dydt = np.zeros(4)
    ### START YOUR CODE HERE ###
    vx, vy, v2 = y[0], y[1], y[0]**2+y[1]**2
    v = np.sqrt(v2)
    ax = -(vx/v)*((y[2]*v2)/m)
    ay = -(vy/v)*((y[3]*v2)/m) - g
    dydt[0], dydt[1] = vx, vy
    dydt[2], dydt[3] = ax, ay
    #### END YOUR CODE HERE ####
    return dydt

def flight_distance(theta, v0, k):
    distance = 0.
    ### START YOUR CODE HERE ###
    height = 0.
    t, t_step = 0, 0.1
    vx, vy = v0*np.cos(theta), v0*np.sin(theta)
    y = np.array([vx, vy, k, k])
    while height >= 0:
        sol = solve_ivp(f, [t,t+t_step], y)
        print ("sol", sol)
        y = sol.y[:,-1]
        t = sol.t[-1]
        dx, dy = y[0], y[1]
        #vx = vx + y[2]
        #vy = vy + y[3]
        y = np.array([vx, vy, k, k])
        distance = distance + dx
        height = height + dy
        print ("time    ", t)
        print ("distance", distance)
        print ("height  ", height)
    #### END YOUR CODE HERE ####
    return distance

flight_distance(np.pi * 0.25, 5, 0)
