import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
fig, axs = plt.subplots(2,1,figsize=(8, 6))
plt.subplots_adjust(hspace=0.5)
#fig, axs = plt.subplots(2,1,sharex=True,figsize=(8, 6))

if False:
   X0 = np.random.uniform(0.,1.,200)
   Y0 = np.random.uniform(0.,1.,200)
   X1 = np.random.uniform(0.,1.,200)
   Y1 = np.random.uniform(0.,1.,200)
   np.savez('randoms.npz', X0=X0, Y0=Y0, X1=X1, Y1=Y1)
else:
   data = np.load('randoms.npz')
   X0 = data['X0']
   Y0 = data['Y0']
   X1 = data['X1']
   Y1 = data['Y1']

inter=[0.0,0.25,0.5,0.75,1.0]

C0_I0=((0.   < X0) & (X0 < 0.25)).sum()
C0_I1=((0.25 < X0) & (X0 < 0.5 )).sum()
C0_I2=((0.5  < X0) & (X0 < 0.75)).sum()
C0_I3=((0.75 < X0) & (X0 < 1.0 )).sum()

C1_I0=((0.   < X1) & (X1 < 0.25)).sum()
C1_I1=((0.25 < X1) & (X1 < 0.5 )).sum()
C1_I2=((0.5  < X1) & (X1 < 0.75)).sum()
C1_I3=((0.75 < X1) & (X1 < 1.0 )).sum()

dx=0.125
x_labels_pos=[0.+dx,0.25+dx,0.5+dx,0.75+dx]
x_labels=[r"$I_0$",r"$I_1$",r"$I_2$",r"$I_3$"]
x_range_pos=inter
x_range_labels=[r"$-30\%$","",r"$p_1^*$","",r"$+30\%$"]
#x_range_labels=[r"$p_1^{*,-30\%}$","",r"$p_1^*$","",r"$p_1^{*,+30\%}$"]
y_range_pos=[0.0,0.5,1.0]
y_range_labels=[r"$-30\%$",r"$p_2^*$" ,r"$+30\%$"]
#y_range_labels=[r"$p_2^{*,-30\%}$",r"$p_2^*$" ,r"$p_2^{*,+30\%}$"]

ax=axs[0]
ax.scatter(X0,Y0, color='g',marker='o',alpha=0.3) # nonsteady configurations
ax.scatter(X1,Y1, color='k',marker='+',alpha=0.3) #    steady configurations
ax.set_xticks(x_labels_pos,minor=True)
ax.set_xticklabels(x_labels,minor=True)
ax.set_xticks(x_range_pos)
ax.set_xticklabels(x_range_labels)
ax.tick_params(axis='x', which='major', pad=15)
ax.set_yticks(y_range_pos)
ax.set_yticklabels(y_range_labels)
#ax.set_aspect('equal', 'box')
ax.set_box_aspect(1)
ax.grid(axis='x', color='k', alpha=1.0,linestyle='--', linewidth=2)
trans = mtransforms.ScaledTranslation(-20/72, 7/72, fig.dpi_scale_trans)
ax.text(0.0, 1.0, "a)", transform=ax.transAxes + trans,
            fontsize='medium', va='bottom', fontfamily='serif')
############################
ax=axs[1]

counts=[C0_I0/(C0_I0+C1_I0),
        C0_I1/(C0_I1+C1_I1),
        C0_I2/(C0_I2+C1_I2),
        C0_I3/(C0_I3+C1_I3)]
ax.hlines(counts[0],inter[0],inter[1],colors="k", linestyles='solid')
ax.hlines(counts[1],inter[1],inter[2],colors="k", linestyles='solid')
ax.hlines(counts[2],inter[2],inter[3],colors="k", linestyles='solid')
ax.hlines(counts[3],inter[3],inter[4],colors="k", linestyles='solid')
ax.hlines(      0.5,     0.0,     1.0,colors="r", linestyles='dashed')
#ax.scatter(X0,Y0, color='r',marker='o',alpha=0.3)
#ax.scatter(X1,Y1, color='k',marker='+',alpha=0.3)
#ax.set_xticks(x_labels_pos,minor=True)
#ax.set_xticklabels(x_labels,minor=True)
ax.set_xticks(x_range_pos)
ax.set_xticklabels(x_range_labels)
ax.tick_params(axis='x', which='major', pad=15)
ax.set_yticks([0,0.5,1.0])
ax.set_yticklabels([r"$0\%$", r"$50\%$", r"$100\%$"])
ax.set_ylabel("Non stationary solutions")
#ax.set_aspect('equal', 'box')
ax.set_box_aspect(1)
ax.grid(axis='x', color='k', alpha=1.0,linestyle='--', linewidth=2)
#pos1=axs[1].get_position()
#pos0=axs[0].get_position()
#ax.set_position([pos0.bounds[0],pos1.bounds[1],pos1.bounds[2],pos1.bounds[3]])
trans = mtransforms.ScaledTranslation(-20/72, 7/72, fig.dpi_scale_trans)
ax.text(0.0, 1.0, "b)", transform=ax.transAxes + trans,
            fontsize='medium', va='bottom', fontfamily='serif')
for ax in axs:
    ax.set_anchor('W')

plt.savefig("methods_histograms.png")
