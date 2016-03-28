# Matrix Algebra
import numpy as np

A = np.matrix([[1, 2, 3], [2, 7, 4]])

B = np.matrix([[1, -1], [0, 1]])

C = np.matrix([[5, -1], [9, 1], [6, 0]])

D = np.matrix([[3, -2, -1], [1, 2, 3]])

u = np.array([6, 2, -3, 5])

v = np.array([3, 5, -1, 4])

w = np.matrix([[1], [8], [0], [5]])

alpha = 6



#Matrix Dimensions
A.shape #1.1: (2 x 3)
B.shape #1.2: (2 x 2)
C.shape #1.3: (3 x 2)
D.shape #1.4: (2 x 3)
u.shape #1.5: (1 x 4)
w.shape #1.6: (4 x 1)

#Vector Operations
np.add(u, v) #2.1: [9, 7, -4, 9]
np.subtract(u, v) #2.2: [3, -3, -2, 1]
np.multiply(alpha, u) #2.3: [36, 12, -18, 30]
np.vdot(u, v) #2.4: 51
np.linalg.norm(u) #2.5: 8.602326704

#Matrix Operations
A + B #3.1: not defined
np.subtract(A, C.T)#3.2: [[-4, -7, -3],[ 3,  6,  4]]
np.add(C.T, (np.multiply(3, D)))#3.3: [[14, 3, 3],[2, 7, 9]]
B * A #3.4: [[-1, -5, -1],[2, 7, 4]]
B * A.T #3.5: not defined
B * C #3.6: not defined
C * B #3.7: [[5, 4], [9, -7], [6, -6]]
B ** 4 #3.8: [[1, -4], [0, 1]]
A * A.T #3.9: [[14, 28], [28, 69]]
D.T * D 
#3.10: I keep getting a ValueError for this and am not sure how to correct it. 
#The answer should be [[10, -4, 6], [-4, 8, 4], [0, 8,8]] 
