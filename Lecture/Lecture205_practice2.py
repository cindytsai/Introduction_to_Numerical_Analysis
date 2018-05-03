import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

xmin, xmax, xbinwidth = 0.,1.,0.05
vx = np.linspace(0.,1.,21)
vy = np.array(
[ 0.981, 0.930, 0.900, 0.889, 0.978, 1.053, 1.000,
  0.986, 1.144, 1.188, 1.309, 1.259, 1.348, 1.435,
  1.427, 1.540, 1.426, 1.203, 0.843, 0.576, 0.060])
vyerr = np.array(
[ 0.044, 0.042, 0.037, 0.037, 0.043, 0.046, 0.038,
  0.045, 0.041, 0.041, 0.044, 0.043, 0.043, 0.041,
  0.050, 0.055, 0.052, 0.074, 0.060, 0.068, 0.082])

x2 = np.polyfit(vx, vy, 2)
x3 = np.polyfit(vx, vy, 3)
x4 = np.polyfit(vx, vy, 4)
x5 = np.polyfit(vx, vy, 5)

plt.errorbar(vx, vy, vyerr, c='blue', fmt = 'o', label = 'data')
plt.plot(vx, np.polyval(x2, vx), label = 'x2')
plt.plot(vx, np.polyval(x3, vx), label = 'x3')
plt.plot(vx, np.polyval(x4, vx), label = 'x4')
plt.plot(vx, np.polyval(x5, vx), label = 'x5')
plt.legend(loc = 2)
plt.show()
