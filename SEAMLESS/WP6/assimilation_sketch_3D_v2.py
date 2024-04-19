import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def GAUSS(x,a,x0,b):
    y=a*np.exp(-(x-x0)**2./b)
    return y

x1   = np.linspace(-5.,5.,100)
y1  = -0.5*x1+3
z1  = GAUSS(x1,1.,1.,0.5)
z2  = GAUSS(x1,1.,2.,1.1)

plt.figure()
ax = plt.subplot(projection='3d')

ax.plot(x1, y1, z1, color='k')
ax.plot(x1, y1, z2, color='k')
#ax.plot(x, y2, z, color='g')
#ax.plot(x, y3, z, color='b')

#ax.add_collection3d(plt.fill_between(x1, 0.5*z1, 0, color='r', alpha=0.3), zs=1, zdir='y')
#ax.add_collection3d(plt.fill_between(x, 0.90*z, 1.10*z, color='g', alpha=0.3), zs=2, zdir='y')
#ax.add_collection3d(plt.fill_between(x, 0.85*z, 1.15*z, color='b', alpha=0.3), zs=3, zdir='y')

ax.set_xlim([-5.,5.])
ax.set_ylim([-5.,5.])
ax.set_xlabel('V1')
ax.set_ylabel('V2')
ax.set_zlabel('Probability')
plt.show()
