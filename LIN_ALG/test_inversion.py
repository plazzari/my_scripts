import numpy as np
from numpy.linalg import inv


a = np.array([[1., 2.], [3., 4.]])
print(a) 
try:
    ainv = inv(a)
    print(ainv) 
except:
    print('singular matrix')


b = np.array([[1., 0.], [1., 0.]])
print(b)
try:
    binv = inv(b)
    print(binv)
except:
    print('singular matrix')

dt=0.01
dx=0.1
k=100.
FD=1.0-2.0*k*dt/dx/dx
FL=k*dt/dx/dx
FR=k*dt/dx/dx
d=np.array([[-1./dx,1./dx,0.], [FL,FD,FR], [0.,-1./dx,1./dx]])

print(d)
try:
    dinv = inv(d)
    print(dinv)
except:
    print('singular matrix')

# NxN Matrix
N=10
dt=0.01
dx=0.1
k=100.
FD=1.0-2.0*k*dt/dx/dx
FL=k*dt/dx/dx
FR=k*dt/dx/dx
M=np.zeros((N,N))
for i in range(N):
    for j in range(N):
        if i==0:
           M[0,0] =-1./dx
           M[0,1] = 1./dx
        elif i == N-1:
           M[N-1,N-2] =-1./dx
           M[N-1,N-1] = 1./dx
        else:
           M[i,i-1] =FL
           M[i,i]   =FD
           M[i,i+1] =FR
print(M)
try:
    Minv = inv(M)
    print(Minv)
except:
    print('singular matrix')
