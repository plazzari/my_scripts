import sys

import argparse
def argument():
    parser = argparse.ArgumentParser(description = '''
    Script to manage restart in a OGSTM 3D simulation
    It sets automatically start and end times, and restarts
    at the end of the simulation.
    ''',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(   '--input_mesh', '-im',
                                type = str,
                                required = False,
                                default="/g100_work/OGS_devC/SSPADA/GHOSH/T1/wrkdir/MODEL/meshmask.nc",
                                help = ''' input meshmask file'''

                                )

    parser.add_argument(   '--input_file', '-i',
                                type = str,
                                required = False,
                                help = ''' input file name'''

                                )

    parser.add_argument(   '--start_date', '-sd',
                                type = str,
                                required = False,
                                default="20190101-000000",
                                help = ''' starting date'''

                                )

        parser.add_argument(   '--variable_name', '-var',
                                type = str,
                                default="20190101-000000",
                                help = ''' Variable name'''

                                )

    return parser.parse_args()

args = argument()

import os,sys
import glob
import datetime
from dateutil.relativedelta import relativedelta
import numpy as np
import netCDF4 as NC
from config import SUBlist
from commons.mask import Mask
from commons.submask import SubMask
import pandas as pd
from commons.interpolators import shift

def smoother2D(mask,RST):
    NsmoothingCycles = 20
    jpj,jpi = mask.shape
    RST[mask ==0 ] = np.nan
    auxs = np.zeros((5,jpj,jpi),np.float32)
    for _ in range(NsmoothingCycles):
        auxs[0,:,:] = RST
        auxs[1,:,:] = shift(RST,1,'r')
        auxs[2,:,:] = shift(RST,1,'l')
        auxs[3,:,:] = shift(RST,1,'u')
        auxs[4,:,:] = shift(RST,1,'d')
        RST = np.nanmean(auxs,axis=0)
    return RST


TheMask = Mask(args.input_mesh)

with NC.Dataset(args.input_mesh,"r") as ncMM:
     jpi     = ncMM.dimensions['x'].size # Longitude
     jpj     = ncMM.dimensions['y'].size # Latitude
     jpk     = ncMM.dimensions['z'].size # Latitude
     tmask   = ncMM.variables['tmask'][0,:,:,:]
     depthM  = ncMM.variables['nav_lev'][:]


ref = datetime.datetime(2019, 1, 1, 0, 0, 0)

indata=np.zeros((jpk,jpj,jpi),dtype=np.double) 
indata_s=np.zeros((jpk,jpj,jpi),dtype=np.double) 

date_list = []

for myt in range(52):
    step = datetime.timedelta(days=int(7*myt))
    date_list.append(ref + step)

for my_date in date_list:
    yyyymmdd=my_date.strftime("%Y%m%d") 
    for isub, sub in enumerate(SUBlist):
       print(sub)
       df      = pd.read_csv(args.input_file, sep="\t",skiprows = 0, engine='python')
       depth   = df['depth'].values
       profile = df[sub].values
       profile_int=np.interp(depthM,depth,profile)
       
       S =SubMask(sub, maskobject=TheMask)
       for k in range(jpk):
          submask = S.mask[k,:,:]
          indata[k,submask] = profile_int[k]
          indata_s[k,:,:] = smoother2D(tmask[k,:,:],indata[k,:,:]) # smoothed indata

    indata_s[tmask == 0] = 1.e20
    filenc="/g100_scratch/userexternal/grosati0/RST." + yyyymmdd + "-00:00:00." + args.variable_name + ".nc"

    with NC.Dataset(filenc,"w") as ncOUT:
         ncOUT.createDimension('x',jpi); # Longitude
         ncOUT.createDimension('y',jpj); # Latitude
         ncOUT.createDimension('time',1);
    
         ncvar = ncOUT.createVariable(var,'d',('time','y','x'))
         ncvar[:]=indata_s
