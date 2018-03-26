import numpy as np

A = np.random.rand(10,10)
B = np.random.rand(10,10)

A_in_det = np.linalg.inv(A)
A_in_det = np.linalg.det(A_in_det)
A_det_in = np.linalg.det(A)
A_det_in = 1./A_det_in
print ("|A^-1| = ", A_in_det)
print ("|A|^-1 = ", A_det_in)
print ("#1 Difference :", round(A_in_det - A_det_in, 5))

A_T_in = A.T
A_T_in = np.linalg.inv(A_T_in)
A_in_T = np.linalg.inv(A)
A_in_T = A_in_T.T
print ("(A.T)^-1")
print (A_T_in)
print ("(A^-1).T")
print (A_in_T)
print ("#2 Difference :")
print (np.round(A_T_in - A_in_T, 5))

AB_in = np.dot(A,B)
AB_in = np.linalg.inv(AB_in)
B_in = np.linalg.inv(B)
A_in = np.linalg.inv(A)
Bin_Ain = np.dot(B_in, A_in)
print ("(AB)^-1")
print (AB_in)
print ("B^-1.A^-1")
print (Bin_Ain)
print ("#3 Difference")
print (np.round(AB_in - Bin_Ain, 5))