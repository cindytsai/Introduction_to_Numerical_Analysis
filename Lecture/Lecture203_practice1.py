import numpy as np
import numpy.matlib
a = np.ones(25)
a[6:9] = a[11:14] = a[16:19] = 0
a = a.reshape(5, 5)
print (a)

b = np.arange(1, 26)
b = b % 2
b = b.reshape(5,5)
print (b)

c = np.array([1.,1.,0.,0.])
c = np.append(c, c)
c = np.append(c, c[::-1])
c = c.reshape(4,4)
c = np.matlib.repmat(c,2,2)
print (c)
