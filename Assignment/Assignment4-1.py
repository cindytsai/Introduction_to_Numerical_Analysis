from scipy import optimize
import numpy as np
import math

def f(x):
    func = math.fabs(math.sin(x) / ((x / (2 * math.pi))**x + math.pi / 8.))
    func = func - (x / (2 * math.pi))
    func = func + (x / (2 * math.pi))**2
    func = func - (1. / 2.)
    return func

def f_solver():
    root1 = optimize.newton(f, 0)
    root2 = optimize.newton(f, 3)
    root3 = optimize.newton(f, 3.5)
    root4 = optimize.newton(f, 5)
    root5 = optimize.newton(f, 8)
    return np.array([root1, root2, root3, root4, root5])
