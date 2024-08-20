import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# df=pd.read_csv("CD46_phys_oce_bottle.tab",sep='\t',skiprows=127,engine='python') # original file
df=pd.read_csv("CD46_phys_oce_bottle.tab.filtered",sep='\t',skiprows=0,engine='python')

#List of events
OID=['0305C#4','0405C#8','0605C#6','1105C#6','1305C#3','1905C#2']
#Varialbes to be plotted
var_list=['Chl_tot_[µg/l]', 'Ed_[µmol/m**2/s]','Eu_[µmol/m**2/s]']
label_list=['chlorophyll concentration',
           'downwelling scalar irradiance',
           'upwelling scalar irradiance']

x_sup_lim_ed=[60., 150., 60., 120., 400., 500.]
x_sup_lim_eu=[1., 3., 3., 5., 10., 10.]

vu=0.4

fig, axs = plt.subplots(3, 2,figsize=(10,16))

for i,ev in enumerate(OID):
   #
   if i != 3:
       flnm_forward='/g100_scratch/userexternal/plazzari/TEST/Forward_Adjoint/BUILD/src/output/Euout_' + OID[i] + '.txt'
       Eu_out=np.loadtxt(flnm_forward)
       Euout_par=np.sum(Eu_out[:,4:17],axis=1)/vu

   eventname='CD46_' + OID[i]
   col=i//2
   row=i%2
   ax=axs[col,row]
   df_event = df[df["Event"]==eventname] 

   z   = df_event["Depth_water_[m]"].values
   chl = df_event["Chl_tot_[µg/l]"].values
   Ed  = df_event["Ed_[µmol/m**2/s]"].values * 0.217 # Conversion Einstein to Watt  E2W=0.217
   Eu  = df_event["Eu_[µmol/m**2/s]"].values * 0.217 # Conversion Einstein to Watt  E2W=0.217

   df_event["category"] = pd.cut(df_event["Depth_water_[m]"], [0,10,20,30,40,400], labels=["0-10","10-20","20-30","30-40",">40"]).astype(str)
   df_event["subgroup"] = df_event.groupby(df_event["Depth_water_[m]"].ne(df_event["Depth_water_[m]"].shift()).cumsum()).cumcount()
   #df_bylev = df_event.drop(columns=['Event','Date/Time']).groupby(["category", "subgroup"],as_index=False).mean()
   df_bylev = df_event.drop(columns=['Event','Date/Time']).groupby(["category"],as_index=False).mean()
   try:
       df_bylev.insert(0, "Event", [ev, ev, ev, ev, ev], True)
   except:
       df_bylev.insert(0, "Event", [ev, ev, ev, ev], True)

   print(eventname)
   print(df_bylev)
   print('-----------')

   if i == 0:
       df_tot=df_bylev.copy()   
   else:
       df_tot=pd.concat([df_tot, df_bylev])

   z_lev   = df_bylev['Depth_water_[m]'].values
   chl_lev = df_bylev["Chl_tot_[µg/l]"].values
   Ed_lev  = df_bylev["Ed_[µmol/m**2/s]"].values * 0.217 # Conversion Einstein to Watt  E2W=0.217
   Eu_lev  = df_bylev["Eu_[µmol/m**2/s]"].values * 0.217 # Conversion Einstein to Watt  E2W=0.217

#  if i == 0:
#      lns1=ax.plot(Ed,z,'k--',label=label_list[1])
#      lns2=ax.plot(Eu,z,'k:', label=label_list[2])
#  else:
#      ax.plot(Ed,z,'k--')
#      ax.plot(Eu,z,'k:')

   if i != 3:
       ax.scatter(Euout_par,[0,10,20,30,40],marker='s',c='r')

   ax.set_xlim([0,x_sup_lim_eu[i]])
   ax.invert_yaxis()
   for lev in [10.0,20.,30.,40.]:
       ax.hlines(y=lev,xmin=0,xmax=x_sup_lim_eu[i],color='r', linestyle=':')

   ax.set_ylim([100,0])
   ax.set_xlabel('Scalar irradiance (W m$^{-2}$)')
   axT=ax.twiny()

   if i == 0:
       lns3=axT.plot(chl,z,'k',label=label_list[0])
   else:
       axT.plot(chl,z,'k')

   axT.set_xlim([0,2])
   axT.set_xlabel('Chlorophyll concentration (mg m$^{-3}$)')

   ax.set_box_aspect(1)

#  if i ==0:
#      lns = lns1+lns2+lns3
#      labs = [l.get_label() for l in lns]
#      ax.legend(lns, labs, loc=4)

   ax.set_ylabel('geometric depth (m)')
   ev_str="OID " + ev
   ax.text(-0.1, 1.15, ev_str, transform=ax.transAxes, fontsize=8, verticalalignment='top')
   # plot avere over layers
   axT.scatter(chl_lev,z_lev,marker='^',c='k')
#  ax.scatter(Ed_lev,z_lev,marker='D',c='k')
   ax.scatter(Eu_lev,z_lev,marker='s',c='k')

#plt.tight_layout()
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.1,
                    hspace=0.4)

df_tot.to_csv("tot_bottle_data.csv",sep='\t',index=False)
plt.savefig("prova.png")

