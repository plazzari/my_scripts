# To launch 
# pyload
# module load paraview
# pvpython alignUVW.py

import os,sys, getopt
import glob
import numpy  as np

#sys.path.append('/pico/home/userexternal/plazzari/.config/ParaView/Macros')
#sys.path.append('/cineca/prod/libraries/scipy/0.15.1/python--2.7.9/lib/python2.7/site-packages')
#sys.path.append('/cineca/prod/libraries/matplotlib/1.4.3/python--2.7.9/lib/python2.7/site-packages')
#sys.path.append('/cineca/prod/libraries/numpy/1.9.2/python--2.7.9/lib/python2.7/site-packages')
#sys.path.append('/cineca/prod/compilers/python/2.7.9/none/lib/python2.7/site-packages/')
from maskload import *
from scipy import stats
from mpl_toolkits.basemap import Basemap
map = Basemap(projection='merc',lat_0=38,lon_0=14,\
                                llcrnrlon = -5.3, \
                                llcrnrlat = 28.0, \
                                urcrnrlon = 37, \
                                urcrnrlat = 46.0, \
                                resolution='l')

#baseXY = np.array(map.projtran(lonlat[:,0],lonlat[:,1])).T

LontoMeters=np.zeros((jpi,),np.float)
LattoMeters=np.zeros((jpj,),np.float)

for i in range(jpi):
    xpt,ypt=map(Lon[jpj/2,i],Lat[jpj/2,0])
    LontoMeters[i]=xpt

for j in range(jpj):
    xpt,ypt=map(Lon[0,jpi/2],Lat[j,jpi/2])
    LattoMeters[j]=ypt

np.savetxt('LontoMeters.txt',LontoMeters)
np.savetxt('LattoMeters.txt',LattoMeters)
