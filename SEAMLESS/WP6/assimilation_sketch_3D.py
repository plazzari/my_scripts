import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x   = np.linspace(-2,2,100)
y1  = np.ones(x.size)
y2  = np.ones(x.size)*2
y3  = np.ones(x.size)*3
z1  = np.sin(x*10)
z2   = 10*np.sin(x*10)
z3   = 100*np.sin(x*10)


plt.figure()
ax = plt.subplot(projection='3d')
ax.plot(x, y1, z1, color='r')
ax.plot(x, y2, z2, color='g')
ax.plot(x, y3, z3, color='b')

ax.add_collection3d(plt.fill_between(x, 0.95*z1, 1.05*z1, color='r', alpha=0.3), zs=1, zdir='y')
ax.add_collection3d(plt.fill_between(x, 0.90*z2, 1.10*z2, color='g', alpha=0.3), zs=2, zdir='y')
ax.add_collection3d(plt.fill_between(x, 0.85*z3, 1.15*z3, color='b', alpha=0.3), zs=3, zdir='y')
plt.show()
plt.savefig("prova.png")
