import pandas as pd
import numpy as np

wl_list=[250 ,325 ,350 ,375 ,400 ,425 ,450 ,475 ,500 ,525
        ,550 ,575 ,600 ,625 ,650 ,675 ,700 ,731 ,775 ,850
        ,950 ,1050 ,1150 ,1250 ,1350 ,1450 ,1550 ,1650 ,1750
        ,1900 ,2200 ,2900 ,3700]

myday ="2020-07-13"
myhour="10:00:00"

Ed=np.zeros([2,len(wl_list)])
Es=np.zeros([2,len(wl_list)])

#Ed
for i,wl in enumerate(wl_list):
    Ed[0,i]=wl
    filein="Ed_" + str(wl) + ".txt"
    df = pd.read_csv(filein,sep=' |\t', engine='python',names=["yyyy-mm-dd", "HH-MM-SS", "Ed"])
    daily  = df[df["yyyy-mm-dd"]==myday]   
    hourly = daily[daily["HH-MM-SS"]==myhour]
    Ed[1,i]=hourly['Ed'].values[0]

filename="Ed_"+myday+"_"+myhour.replace(":","-")+".txt"
dict_out = {'wl': Ed[0,:], 'Ed': Ed[1, :]}
df_out   = pd.DataFrame(data=dict_out)
df_out.to_csv(filename,sep= ' ', header=False, index = False)

#Es
for i,wl in enumerate(wl_list):
    Es[0,i]=wl
    filein="Es_" + str(wl) + ".txt"
    df = pd.read_csv(filein,sep=' |\t', engine='python',names=["yyyy-mm-dd", "HH-MM-SS", "Es"])
    daily  = df[df["yyyy-mm-dd"]==myday]   
    hourly = daily[daily["HH-MM-SS"]==myhour]
    Es[1,i]=hourly['Es'].values[0]

filename="Es_"+myday+"_"+myhour.replace(":","-")+".txt"
dict_out = {'wl': Es[0,:], 'Es': Es[1, :]}
df_out   = pd.DataFrame(data=dict_out)
df_out.to_csv(filename,sep= ' ', header=False, index = False)


