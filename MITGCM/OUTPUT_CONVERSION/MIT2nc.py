import netCDF4 as NC
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

    parser.add_argument(   '--input_file', '-i',
                                type = str,
                                required = True,
                                help = ''' input file name'''

                                )

    parser.add_argument(   '--start_date', '-sd',
                                type = str,
                                required = True,
                                default="20060101-000000",
                                help = ''' starting date'''

                                )

    parser.add_argument(   '--time_step', '-ts',
                                type = int,
                                required = True,
                                help = ''' time step'''

                                )
    return parser.parse_args()

args = argument()

import os,sys
import glob
import datetime
from dateutil.relativedelta import relativedelta
import numpy as np


#file example N1p.0003019680.nc
filein    = args.input_file 
time_step = args.time_step

var     = filein.split(".")[0]
counter = int(filein.split(".")[1])

elapsed_seconds=counter*time_step

Exp_start_date_str=args.start_date

print("Scenario Simulation Starting date: " + Exp_start_date_str)

Exp_start_date=datetime.datetime.strptime(Exp_start_date_str, "%Y%m%d-%H%M%S")

file_counter_to_sec = Exp_start_date + relativedelta(seconds=elapsed_seconds)

file_date=file_counter_to_sec.strftime("%Y%m%d-%H%M%S")

newfilename="ave." + file_date + "." + var + ".nc"

jpk=100
jpj=320
jpi=1040

#shutil.copyfile(filein, newfilename )
indata=np.fromfile(filein, dtype='>f4').reshape(jpk,jpj,jpi)

with NC.Dataset(newfilename,"w") as ncOUT:
    ncOUT.createDimension('lon',jpi);
    ncOUT.createDimension('lat',jpj);
    ncOUT.createDimension('depth',jpk);
    ncOUT.createDimension('time',1);

#   ncvar=ncOUT.createVariable('lon','f',('lon',))
#   ncvar[:]=lon
#   ncvar=ncOUT.createVariable('lat','f',('lat',))
#   ncvar[:]=lat


    ncvar = ncOUT.createVariable(var,'f',('time','depth','lat','lon'))
    ncvar[:]=indata

print("converted "  + filein + " to " +  newfilename) 
