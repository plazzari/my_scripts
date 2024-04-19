import sys

import argparse
def argument():
    parser = argparse.ArgumentParser(description = '''
    Script to manage restart in a MITgcm+BFM simulation
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

    parser.add_argument(   '--time_step', '-ts',
                                type = int,
                                required = False,
                                help = ''' time step'''

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

jpj=380
jpi=1085

with NC.Dataset(args.input_mesh,"r") as ncMM:
     jpi     = ncMM.dimensions['x'].size # Longitude
     jpj     = ncMM.dimensions['y'].size # Latitude
     tmask2D = ncMM.variables['tmask'][0,0,:,:]

ref = datetime.datetime(2019, 1, 1, 0, 0, 0)

var="PRMS.light.EPS0r"
PARAMETER_DIR="/g100_work/OGS_devC/V10C/RUNS_SETUP/SEAMLESS/eat_da_pseudo_lagrangian_T17_Backup/PLOTS/PARAMETERS_TXT/"
floatname =[ '6901772','6901774','6901775','6902898','6902902','6902903','6902904','6903247','6903250']
mybasin   =[    'ion2',   'swm2',   'lev1',   'lev2',   'lev2',   'tyr2',   'lev2',   'lev2',   'adr2']

float2sub={'South Western Mediterranean east' : ['6901774'],
           'Southern Tyrrhenian' : ['6902903'],
           'Southern Adriatic' : ['6903250'],
           'Eastern Ionian' : ['6901772'],
           'Western Levantine' : ['6901775'],
           'Northern Levantine' : ['6902898','6902902','6902903','6902904']}

#ion2 Eastern Ionian,
#lev1 Western Levantine,
#lev2 Northern Levantine,

indata=np.zeros((jpj,jpi),dtype=np.double) 
indata[tmask2D == 0] = 1.e20

date_list = []

for myt in range(52):
    step = datetime.timedelta(days=int(7*myt))
    date_list.append(ref + step)

for my_date in date_list:
    yyyymmdd=my_date.strftime("%Y%m%d") 
    for isub, sub in enumerate(SUBlist):
       print(sub)
       if str(sub) in float2sub:
          param=0
          Nfloat=len(float2sub[str(sub)])
          for floatname in float2sub[str(sub)]:
              filein=PARAMETER_DIR+floatname+"_instances_light_parameters_EPS0r_interp.txt"
              df    = pd.read_csv(filein, sep="\t",skiprows = 0, engine='python')
              df1   = df.loc[(df['date'] == int(yyyymmdd))]
              param += df1['AVE'].values
          param=param/Nfloat
          print(param)
       else:
          param=0.04

       S =SubMask(sub, maskobject=TheMask)
       submask = S.mask[0,:,:]
       indata[submask] = param

    indata_s = smoother2D(tmask2D,indata) # smoothed indata
    indata_s[tmask2D == 0] = 1.e20
    filenc="/g100_work/OGS_devC/V10C/RUNS_SETUP/SEAMLESS/T6/wrkdir/MODEL/KEXT/KextF_" + yyyymmdd + "-00:00:00" + ".nc"

    with NC.Dataset(filenc,"w") as ncOUT:
         ncOUT.createDimension('x',jpi); # Longitude
         ncOUT.createDimension('y',jpj); # Latitude
         ncOUT.createDimension('time',1);
    
         ncvar = ncOUT.createVariable('kextfact','f',('y','x'))
         ncvar[:]=indata_s
