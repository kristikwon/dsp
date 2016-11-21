# Matrix Algebra

import numpy as np

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])
alpha = 6

# 1. Matrix Dimensions
print A.shape
print B.shape
print C.shape
print D.shape
print u.shape
print w.shape
"""
Answers for 1.1 - 1.6
(2, 3)
(2, 2)
(3, 2)
(2, 3)
(4,)
(4, 1)
"""

#2. Vector Operations
print u+v
print u-v
print 6 * u
print np.dot(u,v)
print np.linalg.norm(u)
"""
Answers for 2.1 - 2.5
[ 9  7 -4  9]
[ 3 -3 -2  1]
[ 36  12 -18  30]
51
8.60232526704
"""

#3. Matrix Operations
#print A+C
print A - C.transpose()
print C.transpose() + 3*D
print np.dot(B,A)
#print np.dot(B,A.transpose())
#print np.dot(B,C)
print np.dot(C,B)
print np.dot(np.dot(np.dot(B,B),B),B)
print np.dot(A,A.transpose())
print np.dot(D.transpose(),D)
"""
Answers for 3.1 - 3.10
3.1: not defined
3.2: 
[[-4 -7 -3]
 [ 3  6  4]]
3.3:
[[14  3  3]
 [ 2  7  9]]
3.4:
[[-1 -5 -1]
 [ 2  7  4]]
3.5: not defined
3.6: not defined
3.7:
[[ 5 -6]
 [ 9 -8]
 [ 6 -6]]
3.8:
[[ 1 -4]
 [ 0  1]]
3.9:
[[14 28]
 [28 69]]
3.10:
[[10 -4  0]
 [-4  8  8]
 [ 0  8 10]]
"""

