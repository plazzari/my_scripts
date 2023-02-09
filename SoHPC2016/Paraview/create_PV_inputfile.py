# To launch 
# module load paraview
# pvpython alignUVW.py

import os,sys, getopt
import glob
import numpy  as np

from maskload import *
from scipy import stats


filenameU='/pico/scratch/userexternal/plazzari/xVISUALIZZAZIONE3d/FORCINGS/OUTPUT/U20140926-12:00:00.nc'
filenameV='/pico/scratch/userexternal/plazzari/xVISUALIZZAZIONE3d/FORCINGS/OUTPUT/V20140926-12:00:00.nc'
filenameW='/pico/scratch/userexternal/plazzari/xVISUALIZZAZIONE3d/FORCINGS/OUTPUT/W20140926-12:00:00.nc'

U        =  NC.netcdf_file(filenameU,"r",mmap=False)
V        =  NC.netcdf_file(filenameV,"r",mmap=False)
W        =  NC.netcdf_file(filenameW,"r",mmap=False)

dataU    = (U.variables["vozocrtx"].data[0,0:jpk,0:jpj,0:jpi])
dataV    = (V.variables["vomecrty"].data[0,0:jpk,0:jpj,0:jpi])
dataW    = (W.variables["vovecrtz"].data[0,0:jpk,0:jpj,0:jpi])

for jk in range(jpk):
  for jj in range(jpj):
     for ji in range(jpi):
         if (dataU[jk,jj,ji] > 10000.): dataU[jk,jj,ji]=np.NaN
         if (dataV[jk,jj,ji] > 10000.): dataV[jk,jj,ji]=np.NaN
         if (dataW[jk,jj,ji] > 10000.): dataW[jk,jj,ji]=np.NaN


aux = np.zeros([jpk,jpj,1])*np.NaN;     dataUp1  = np.append(dataU,aux,2)
aux = np.zeros([jpk,1,jpi])*np.NaN;     dataVp1  = np.append(dataV,aux,1)
aux = np.zeros([1,jpj,jpi])*np.NaN;     dataWp1  = np.append(dataW,aux,0)

dataUp1r = dataUp1.copy()         ;     dataUp1r = np.roll(dataUp1r,1,axis=2); dataUp1r[:,:,0]=np.NaN
dataVp1r = dataVp1.copy()         ;     dataVp1r = np.roll(dataVp1r,1,axis=1); dataVp1r[:,0,:]=np.NaN
dataWp1r = dataWp1.copy()         ;     dataWp1r = np.roll(dataWp1r,-1,axis=0);dataWp1r[jpk-1,:,:]=np.NaN

dataUint = stats.nanmean( np.array([dataUp1r,dataUp1]),axis=0)
dataVint = stats.nanmean( np.array([dataVp1r,dataVp1]),axis=0)
dataWint = stats.nanmean( np.array([dataWp1r,dataWp1]),axis=0)

dataUint[np.isnan(dataUint)] = 10.**20


from paraview.simple import *
import vtk

rg = vtk.vtkRectilinearGrid()
rg.SetDimensions(jpi,jpj,jpk)

daLon=vtk.vtkFloatArray()
daLat=vtk.vtkFloatArray()
daDep=vtk.vtkFloatArray()

daLon.SetNumberOfComponents(1)
daLat.SetNumberOfComponents(1)
daDep.SetNumberOfComponents(1)

daLon.SetNumberOfTuples(jpi)
daLat.SetNumberOfTuples(jpj)
daDep.SetNumberOfTuples(jpk)

LontoMeters=np.loadtxt('LontoMeters.txt')
LattoMeters=np.loadtxt('LattoMeters.txt')

for i in range(jpi):
    daLon.SetTuple1(i,-1.* LontoMeters[i])
#   daLon.SetTuple1(i,LontoMeters[i])

for j in range(jpj):
    daLat.SetTuple1(j,LattoMeters[j])

for k in range(jpk):
    daDep.SetTuple1(k,1000.*nav_lev[k])
#   daDep.SetTuple1(k,nav_lev[k])

rg.SetXCoordinates(daLon)
rg.SetYCoordinates(daLat)
rg.SetZCoordinates(daDep)

jpim1=jpi-1
jpjm1=jpj-1
jpkm1=jpk-1

u1 = vtk.vtkFloatArray()
u1.SetName("u1")
u1.SetNumberOfComponents(1)
u1.SetNumberOfTuples((jpim1)*(jpjm1)*(jpkm1))

#....... riempi il tuo vettore 
for z in range(jpk-1):
    for y in range(jpj-1):
        for x in range(jpi-1):
            u1.SetTuple1(x+y*jpim1+z*jpim1*jpjm1, dataUint[z,y,x] ) # 

rg.GetCellData().AddArray(u1)

v1 = vtk.vtkFloatArray()
v1.SetName("v1")
v1.SetNumberOfComponents(1)
v1.SetNumberOfTuples((jpim1)*(jpjm1)*(jpkm1))

#....... riempi il tuo vettore 
for z in range(jpk-1):
    for y in range(jpj-1):
        for x in range(jpi-1):
            v1.SetTuple1(x+y*jpim1+z*jpim1*jpjm1, dataVint[z,y,x] ) # 

rg.GetCellData().AddArray(v1)

w1 = vtk.vtkFloatArray()
w1.SetName("w1")
w1.SetNumberOfComponents(1)
w1.SetNumberOfTuples((jpim1)*(jpjm1)*(jpkm1))

#....... riempi il tuo vettore 
for z in range(jpk-1):
    for y in range(jpj-1):
        for x in range(jpi-1):
            w1.SetTuple1(x+y*jpim1+z*jpim1*jpjm1, dataWint[z,y,x] ) # 

rg.GetCellData().AddArray(w1)

rgw = vtk.vtkXMLRectilinearGridWriter()
rgw.SetFileName("testUVWC.vtr")
rgw.SetInputData(rg)
rgw.Write()
