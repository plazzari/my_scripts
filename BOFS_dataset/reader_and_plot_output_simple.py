import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#List of events
TEST=['','TEST_2','TEST_3','TEST_4','TEST_5','TEST_6']
#Varialbes to be plotted
var_list=['Chl_tot_[µg/l]', 'Ed_[µmol/m**2/s]','Eu_[µmol/m**2/s]']
label_list=['chlorophyll concentration',
           'downwelling scalar irradiance',
           'upwelling scalar irradiance']

x_sup_lim_ed=[60., 150., 60., 120., 400., 500.]
x_sup_lim_eu=[1., 3., 3., 5., 10., 10.]

vu=0.4

fig, axs = plt.subplots(3, 2,figsize=(10,16))

for i,ev in enumerate(TEST):
    flnm_forward='/g100_work/OGS23_PRACE_IT/plazzari/Forward_Adjoint_neccton/BUILD/src/output/Edout_' + TEST[i] + '.txt'
    Edir_out=np.loadtxt(flnm_forward)
    Edirout_par=np.sum(Edir_out[:,4:17],axis=1)/vd

    flnm_forward='/g100_work/OGS23_PRACE_IT/plazzari/Forward_Adjoint_neccton/BUILD/src/output/Esout_' + TEST[i] + '.txt'
    Es_out=np.loadtxt(flnm_forward)
    Esout_par=np.sum(Es_out[:,4:17],axis=1)/vs

    Edout_par=Edirout_par+Esout_par
   #
    flnm_forward='/g100_work/OGS23_PRACE_IT/plazzari/Forward_Adjoint_neccton/BUILD/src/output/Euout_' + TEST[i] + '.txt'
    Eu_out=np.loadtxt(flnm_forward)
    Euout_par=np.sum(Eu_out[:,4:17],axis=1)/vu

    z_forward='/g100_work/OGS23_PRACE_IT/plazzari/Forward_Adjoint_neccton/BUILD/src/z.txt'
    z=np.loadtxt(z_forward)

    col=i//2
    row=i%2
    ax=axs[col,row]

    print(eventname)
    print('-----------')


    ax.scatter(Euout_par,[0,10,20,30,40],marker='s',c='r')

    ax.set_xlim([0,x_sup_lim_eu[i]])
    ax.invert_yaxis()
    for lev in [10.0,20.,30.,40.]:
        ax.hlines(y=lev,xmin=0,xmax=x_sup_lim_eu[i],color='r', linestyle=':')

    ax.set_ylim([100,0])
    ax.set_xlabel('Scalar irradiance (W m$^{-2}$)')
    axT=ax.twiny()

    ax.set_ylabel('geometric depth (m)')
    ev_str=  ev
    ax.text(-0.1, 1.15, ev_str, transform=ax.transAxes, fontsize=8, verticalalignment='top')
   # plot avere over layers
#  ax.scatter(Ed_lev,z_lev,marker='D',c='k')

#plt.tight_layout()
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.1,
                    hspace=0.4)

plt.savefig("prova.png")

