import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():
    # Based on "Stove Ownership" from XKCD by Randall Munroe
    # https://xkcd.com/418/

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
#   ax.spines[['top', 'right']].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim([-30, 10])

    data = np.ones(100)
    data[:] -= np.arange(100)

    print(data)

    ax.annotate(
        'SLOPE',
        xy=(25, -20.), arrowprops=dict(arrowstyle='->'), xytext=(40, -10))

    ax.plot(data)

    ax.set_xlabel('log(ESD)')
    ax.set_ylabel('log(Biomass)')

#   fig.text(
#       0.5, 0.05,
#       '"Stove Ownership" from xkcd by Randall Munroe',
#       ha='center')
plt.savefig('slope.png')
