import argparse
import os,sys
import glob
import datetime
from dateutil.relativedelta import relativedelta
import numpy as np
import netCDF4

def argument():
    parser = argparse.ArgumentParser(description = '''
    Script to manage restart in a MITgcm+BFM simulation
    It sets automatically the BFM forcing files such as
    CO2 files, extinction coeff. and rivers runoff  data
    ''',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(   '--iteration', '-it',
                                type = int,
                                required = True,
                                help = ''' interation index'''

                                )
    parser.add_argument(   '--start_date', '-sd',
                                type = str,
                                required = False,
                                default="20060101-000000",
                                help = ''' starting date'''

                                )
    parser.add_argument(   '--months_increment', '-mi',
                                type = int,
                                required = True,
                                default=1,
                                help = ''' months increment'''

                                )
    parser.add_argument(   '--end___date', '-ed',
                                type = str,
                                required = False,
                                default="21000101-000000",
                                help = ''' starting date'''

                                )
    parser.add_argument(   '--output_nectdf', '-on',
                                type = bool,
                                required = False,
                                default=False,
                                help = ''' option to write also netcdf'''

                                )

    return parser.parse_args()

def create_data_BFMcoupler_namelist(start_month,end___month,delta_month):
    filein="data.BFMcoupler.template"
    fileout="data.BFMcoupler"
    f = open(filein,'r')
    filedata = f.read()
    f.close()

    BFMcoupler_forcingPeriod = 2628000. #30.5 days in seconds
    BFMcoupler_forcingCycle  = BFMcoupler_forcingPeriod*(delta_month+2)
#   BFMcoupler_forcingCycle  = 36792000.,

    f = open(fileout,'w')
    newdata = filedata.replace("@start_month",str(start_month))
    newdata = newdata.replace("@end___month",str(end___month))
    newdata = newdata.replace("@BFMcoupler_forcingPeriod",str(BFMcoupler_forcingPeriod))
    newdata = newdata.replace("@BFMcoupler_forcingCycle",str(BFMcoupler_forcingCycle))
    f.write(newdata)
    f.close()

'''
from netCDF4 import Dataset
'''
def readfile(filename, var):
    '''
    Generic file reader
    '''
    D = netCDF4.Dataset(filename,"r")
    VAR = np.array(D. variables[var])
    D.close()
    return VAR
args = argument()


iteration=args.iteration # Iteration starts from 0


Exp_start_date_str=args.start_date
print("Scenario Simulation Starting date: " + Exp_start_date_str)
Exp___end_date_str=args.end___date
print("Scenario Simulation End      date: " + Exp___end_date_str)

Exp_start_date=datetime.datetime.strptime(Exp_start_date_str, "%Y%m%d-%H%M%S")
Exp___end_date=datetime.datetime.strptime(Exp___end_date_str, "%Y%m%d-%H%M%S")

NYEARS=Exp___end_date.year - Exp_start_date.year + 1
NMAX = 12 * NYEARS

print(" Total number of years           :" + str(NYEARS))
print(" Total number of months          :" + str(NMAX))

delta_month=args.months_increment

start_months=delta_month*iteration
end___months=delta_month*(iteration+1)

start_simulation_date = Exp_start_date + relativedelta(months=start_months)
end___simulation_date = Exp_start_date + relativedelta(months=end___months)

start_simulation_date_str=start_simulation_date.strftime("%Y%m%d-%H%M%S")
end___simulation_date_str=end___simulation_date.strftime("%Y%m%d-%H%M%S")

print("Starting iteration #: "     + str(iteration))
print("Simulation Start    date: " + start_simulation_date_str)
print("imulation end      date: "  + end___simulation_date_str)


print('boom')

anno1=Exp_start_date.year
anno2=Exp___end_date.year
nmesi=12
nanni=anno2-anno1+1
numerodati=nanni
nmesi=12

nxgm=1040
nygm=320
nzgm=100
###
data = np.fromfile('XC.data', dtype=">f4", count=-1)
XC=np.reshape(data, (320, 1040))

data = np.fromfile('YC.data', dtype=">f4", count=-1)
YC=np.reshape(data, (320, 1040))

data = np.fromfile('RC.data', dtype=">f4", count=-1)
RC=np.reshape(data, (100))

RC=RC*-1

data = np.fromfile('hFacC.data', dtype=">f4", count=-1)
maskgm=np.reshape(data, (100,320,1040))

maskgm=maskgm.astype(float)
maskgm[maskgm==0]=np.nan

print(RC)
######

DATADIR= "../inputRIVER-BC/"

name=['Co2','KEXT','RIVER_ALK_GmolperYR_NOBLS','RIVER_DIC_KTperYR_NOBLS','RIVER_DIN_KTperYR_NOBLS','RIVER_DIP_KTperYR_NOBLS','RIVER_DIS_KTperYR_NOBLS','RIVER_O2o_GmolperYR_NOBLS']
for ss,ssm in enumerate(name):
#   filedaleggere="%s%s"%(ssm,'_RCP8_5__monthly_2006_2100.bin')
    filedaleggere=DATADIR+ssm+"_RCP8_5__monthly_2006_2100.nc"
    field=readfile(filedaleggere, ssm)
#   data=np.fromfile(filedaleggere, dtype=">f4", count=-1)
    print(np.shape(field))
#   field=np.reshape(data,(12*nanni,320,1040))
    bfm=np.zeros((delta_month+2,nygm,nxgm),np.float32)
#   pickupfrequency=2592000
#   frequncydadato=0# numero di iterazioni da file pickup (numero nel nome)
#   timestep=20# guarda in data
    mesedaricominciare=start_months#se il pickup è salvato mensilmente ...questo è da modificare frose..
#   mesedaricominciare=int(np.round(timestep*frequncydadato/pickupfrequency))#se il pickup è salvato mensilmente ...questo è da modificare frose..
    kount=0
    print(mesedaricominciare)
#   for iy in range(nanni):
#       for ll in range(nmesi):
#           if kount==mesedaricominciare and kount<=11: #se siamo ancora nel primo anno di simulazione
#              M_2D=field[0,:,:]
#              endfield=M_2D
#           if kount==mesedaricominciare and kount>11:#prendiamo il mese precedente per interpolare 
#              M_2D=field[kount-1,:,:]
#              endfield=M_2D
#           if kount>=mesedaricominciare and kount<=mesedaricominciare+11:# costruiamo la serie nel mezzo (lunga un anno)
#              M_2D=field[kount,:,:]            
#              bfm[kount-mesedaricominciare,:,:]=M_2D[:,:]
#              print(kount)
#           kount+=1
#   bfm[delta_month,:,:]=bfm[,:,:]#penultimo uguale a terzultimo
#   bfm[13,:,:]=endfield[:,:]#ultimo uguale a primoe

    for mm in range(delta_month):
        bfm[mm,:,:] = field[start_months+mm,:,:]

    if start_months+delta_month < NMAX:
        bfm[delta_month,:,:]= field[start_months+delta_month,:,:]
    else:
        bfm[delta_month,:,:]= field[start_months+delta_month-1,:,:]

    if start_months == 0:
        bfm[delta_month+1,:,:]=field[0,:,:]
    else:
        bfm[delta_month+1,:,:]=field[start_months-1,:,:]


#   bfm[12,:,:]=bfm[11,:,:]#penultimo uguale a terzultimo
#   bfm[13,:,:]=endfield[:,:]#ultimo uguale a primoe
#########################################    
   #scrivo
    fileout="%s%s%s%s%s%s"%(ssm,'_',start_months,'_',start_months+delta_month,'_bfm_friend.bin')#python conta sempre meno uno
    fid=open(fileout,'w')
    bfm.byteswap().tofile(fid, sep='')
    fid.close()

    if args.output_nectdf:
       suffix='_.nc'
       fileout="%s%s%s%s%s%s"%(ssm,'_',start_months,'_',start_months+delta_month,'_bfm_friend.nc')
       rootgrp = netCDF4.Dataset(fileout, "w", format="NETCDF4")
       rootgrp.createDimension('lon', nxgm)
       rootgrp.createDimension('lat', nygm)
       rootgrp.createDimension('time', delta_month+2)
       lon = rootgrp.createVariable('lon', 'f4', ('lon',))
       lat = rootgrp.createVariable('lat', 'f4', ('lat',))
       varname= rootgrp.createVariable(str(ssm), 'f8', ('time','lat', 'lon',))
       lat.units='degree_north'
       lon.units='degree_east'
       lat[:] = YC[:,0]
       lon[:] = XC[0,:]
       varname[:,:,:]=bfm[:,:,:]*maskgm[0,:,:]
       rootgrp.close()

create_data_BFMcoupler_namelist(start_months,end___months,delta_month)
print('fatto')
