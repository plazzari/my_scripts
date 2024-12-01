import numpy as np
import matplotlib.pyplot as plt

def Ch(t,w,Smax,t0):
    #characteristic function for diatoms splitting
    C0=np.power(Smax,-3./2.)-1.5*w*t0
    return np.power(1.5*w*t+C0,-2./3.)

w=1.e-06
Nyears=4.
Smax=120.
St=80.

NT=365*int(Nyears)

fig,ax = plt.subplots(1,figsize=(9, 6),gridspec_kw = {'wspace':1.5, 'hspace':1.5})

t0=0.
t1=1000.
t=np.arange(t0,365.*Nyears)
ax.plot(t,Ch(t,w,Smax,t0),c='k',linewidth=4)
ax.vlines(t1,ymin=0.,ymax=St,colors='g', linestyles='--',linewidth=4)

ax.annotate(r'$n(t^1,S_{MAX})$',
            xy=(t1,Smax), xycoords='data',
            xytext=(-10, 10), textcoords='offset points')
#           arrowprops=dict(facecolor='black', shrink=0.05),
#           horizontalalignment='center', verticalalignment='bottom')
ax.scatter(t1,Smax,s=40.,c='k')

ax.set_xlim([0.,NT])
ax.set_ylim([40.,Smax+Smax/10.])
ax.set_yticks([St,Smax])
ax.set_yticklabels([r'$S_T$',r'$S_{MAX}$'])
ax.set_xticks(np.arange(0.,NT,360))
ax.set_xticklabels([])
ax.set_xlabel('time')
ax.set_ylabel('size')

step=100

for t0 in range(0,NT,step):
    t=np.arange(t0,365.*Nyears)
    ax.plot(t,Ch(t,w,Smax,t0),c='k',linewidth=1)

for t0 in range(-365*10,0,step):
    t=np.arange(t0,365.*Nyears)
    ax.plot(t,Ch(t,w,Smax,t0),c='k',linewidth=1)

ax.axhline(y=Smax, color='r', linestyle='--') 

fileout='diatoms_char.png'
fig.savefig(fileout, format='png',dpi=300, bbox_inches="tight")
