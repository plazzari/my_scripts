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
x_sup_lim_eu=[4.0, 10., 4.5, 5., 4.5, 35.]

vd=1.
vu=0.4
vs=0.83

fig, axs = plt.subplots(3, 2,figsize=(10,16))

for i,ev in enumerate(OID):
   #
   if i != 3:
       flnm_forward='/g100_work/OGS23_PRACE_IT/plazzari/Forward_Adjoint_neccton/BUILD/src/output/Edout_' + OID[i] + '.txt'
       Edir_out=np.loadtxt(flnm_forward)
       Edirout_par=np.sum(Edir_out[:,4:17],axis=1)/vd

       flnm_forward='/g100_work/OGS23_PRACE_IT/plazzari/Forward_Adjoint_neccton/BUILD/src/output/Esout_' + OID[i] + '.txt'
       Es_out=np.loadtxt(flnm_forward)
       Esout_par=np.sum(Es_out[:,4:17],axis=1)/vs

       Edout_par=Edirout_par+Esout_par

       flnm_forward='/g100_work/OGS23_PRACE_IT/plazzari/Forward_Adjoint_neccton/BUILD/src/output/Euout_' + OID[i] + '.txt'
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

   if i == 0:
       ax.plot(Ed,z,'k--')#,label=label_list[1])
   else:
       ax.plot(Ed,z,'k--')

   if i != 3:
       lns1=ax.scatter(Edout_par,[0,10,20,30,40],marker='D',c='k',label='Ed model')

   ax.set_xlim([0,x_sup_lim_ed[i]])
   ax.invert_yaxis()

   for lev in [10.,20.,30.,40.]:
       ax.hlines(y=lev,xmin=0,xmax=x_sup_lim_ed[i],color='k', linestyle=':',alpha=0.5)

   ax.set_ylim([100,0])
   ax.set_xlim([0,x_sup_lim_ed[i]])
   ax.set_xlabel('Scalar irradiance (W m$^{-2}$)')
   axT=ax.twiny()

   if i == 0:
       axT.plot(Eu,z,'r:')#, label=label_list[2])
   else:
       axT.plot(Eu,z,'r:')

   if i != 3:
       lns2=axT.scatter(Euout_par,[0,10,20,30,40],marker='s',c='r',label='Eu model')

   axT.set_xlim([0,x_sup_lim_eu[i]])
   axT.set_xlabel('Scalar irradiance (W m$^{-2}$)')

   ax.set_box_aspect(1)

   ax.set_ylabel('geometric depth (m)')
   ev_str="OID " + ev
   ax.text(-0.1, 1.15, ev_str, transform=ax.transAxes, fontsize=8, verticalalignment='top')
   # plot avere over layers
   lns3=ax.scatter(Ed_lev,z_lev,marker='+',c='k',label='Ed Data')
   lns4=axT.scatter(Eu_lev,z_lev,marker='o',c='r', label='Eu Data')
   lines, labels = ax.get_legend_handles_labels()
   linesT, labelsT = axT.get_legend_handles_labels()
   if i ==0:
       axT.legend(lines + linesT, labels + labelsT, loc=4)


#  if i == 0:
#      lns = lns1+lns2+lns3+lns4
#      #lns = lns1+lns2
#      labs = [l.get_label() for l in lns]
#      ax.legend(lns, labs, loc=4)
#plt.tight_layout()
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.1,
                    hspace=0.4)

df_tot.to_csv("tot_bottle_data.csv",sep='\t',index=False)
plt.savefig("Check_output.png")

