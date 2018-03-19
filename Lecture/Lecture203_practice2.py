import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0.,10.,1000)
# parameter
(n, d) = (4.,1.)
k = n / d

x = np.cos(k*t)*np.cos(t)
y = np.cos(k*t)*np.sin(t)

plt.plot(x, y, color = 'red', linewidth = 2, linestyle = '-')
plt.show()
