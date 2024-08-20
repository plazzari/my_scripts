import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("tot_bottle_data.csv",sep='\t',skiprows=0,engine='python')

#List of events
OID=['0305C#4','0405C#8','0605C#6','1105C#6','1305C#3','1905C#2']
#Varialbes to be plotted
var_list=['Chl_tot_[µg/l]', 'Ed_[µmol/m**2/s]','Eu_[µmol/m**2/s]']

Ed_surf=np.array([121.1,297.4,182.6,262.5,946.5,972.8])*0.217


for i,ev in enumerate(OID):

   eventname=OID[i]
   df_event = df[df["Event"]==eventname] 

   z   = df_event["Depth_water_[m]"].values
   chl = df_event["Chl_tot_[µg/l]"].values/4.
   Ed  = df_event["Ed_[µmol/m**2/s]"].values * 0.217 # Conversion Einstein to Watt  E2W=0.217
   Eu  = df_event["Eu_[µmol/m**2/s]"].values * 0.217 # Conversion Einstein to Watt  E2W=0.217

   data={
           "chl1": chl,
           "chl2": chl,
           "chl3": chl,
           "chl4": chl,
        }
   
   df_out = pd.DataFrame(data)
   fileout='OUTPUT/' + eventname + '_chl.txt'
   df_out.to_csv(fileout,sep=" ",index=False,header=False)

   data={
           "C1": chl*50.,
           "C2": chl*50.,
           "C3": chl*50.,
           "C4": chl*50.,
        }

   df_out = pd.DataFrame(data)
   fileout='OUTPUT/' + eventname + '_C.txt'
   df_out.to_csv(fileout,sep=" ",index=False,header=False)

   data={
           "Ed": Ed,
           "Eu": Eu,
        }
   df_out = pd.DataFrame(data)
   fileout='OUTPUT/' + eventname + '_E.txt'
   df_out.to_csv(fileout,sep=" ",index=False,header=False)

   lam=np.array([[ 250,  187.5,  312.5], # 0
               [ 325,  312.5,  337.5],   # 1
               [ 350,  337.5,  362.5],   # 2
               [ 375,  362.5,  387.5],   # 3
               [ 400,  387.5,  412.5],   # 4
               [ 425,  412.5,  437.5],   # 5
               [ 450,  437.5,  462.5],   # 6
               [ 475,  462.5,  487.5],   # 7
               [ 500,  487.5,  512.5],   # 8
               [ 525,  512.5,  537.5],   # 9
               [ 550,  537.5,  562.5],   # 0
               [ 575,  562.5,  587.5],   # 1
               [ 600,  587.5,  612.5],   # 2
               [ 625,  612.5,  637.5],   # 3
               [ 650,  637.5,  662.5],   # 4
               [ 675,  662.5,  687.5],   # 5
               [ 700,  687.5,  712.5],   # 6
               [ 725,  712.5,  750.0],   # 7
               [ 775,  750.0,  800.0],
               [ 850,  800.0,  900.0],
               [ 950,  900.0, 1000.0],
               [1050, 1000.0, 1100.0],
               [1150, 1100.0, 1200.0],
               [1250, 1200.0, 1300.0],
               [1350, 1300.0, 1400.0],
               [1450, 1400.0, 1500.0],
               [1550, 1500.0, 1600.0],
               [1650, 1600.0, 1700.0],
               [1750, 1700.0, 1800.0],
               [1900, 1800.0, 2000.0],
               [2200, 2000.0, 2400.0],
               [2900, 2400.0, 3400.0],
               [3700, 3400.0, 4000.0]])

   dl=lam[4:17,2]-lam[4:17,1]

   filename_Ed="Ed_2020-07-13_10-00-00.txt"
   filename_Es="Es_2020-07-13_10-00-00.txt"

   Ed_OASIM=np.loadtxt(filename_Ed)[:,:]
   Es_OASIM=np.loadtxt(filename_Es)[:,:]

   NORM=sum((Ed_OASIM[4:17,1]+Es_OASIM[4:17,1]))
   Ed_OASIMv2=Ed_OASIM[:,1]/NORM*Ed_surf[i]
   Es_OASIMv2=Es_OASIM[:,1]/NORM*Ed_surf[i]

   filename="OUTPUT/"+ eventname + filename_Ed
   dict_out = {'wl': Ed_OASIM[:,0], 'Ed': Ed_OASIMv2}
   df_out   = pd.DataFrame(data=dict_out)
   df_out.to_csv(filename,sep= ' ', header=False, index = False)

   filename="OUTPUT/"+ eventname + filename_Es
   dict_out = {'wl': Es_OASIM[:,0], 'Ed': Ed_OASIMv2}
   df_out   = pd.DataFrame(data=dict_out)
   df_out.to_csv(filename,sep= ' ', header=False, index = False)

