import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 14,
    "axes.labelsize": 18,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    "legend.fontsize": 14,
    "axes.linewidth": 1.2
})

patterns = ['tm_1111', 'tm_1221', 'tm_1331', 'tm_1441', 'tm_1461', 'tm_1481']

openmpi_bruto = [
    [263.17739223, 260.57538838, 257.55803001],
    [514.10416268, 506.63598439, 509.26518726],
    [736.96766833, 744.33660444, 745.39030279],
    [969.26710117, 967.57270316, 973.01019940],
    [949.15721907, 960.63568013, 960.87737917],
    [941.11875285, 940.28507381, 946.75946427]
]

resipipe_bruto = [
    [255.51209826, 256.02768722, 262.35495998],
    [499.81328475, 499.59869590, 500.33018609],
    [743.64916544, 745.82924768, 755.98469534],
    [978.51328328, 970.82330600, 973.33140668],
    [944.69201912, 962.25393025, 962.88015730],
    [932.98138247, 963.63376474, 956.27273712]
]

openmpi_mean = np.mean(openmpi_bruto, axis=1)
openmpi_std = np.std(openmpi_bruto, axis=1, ddof=1)

resipipe_mean = np.mean(resipipe_bruto, axis=1)
resipipe_std = np.std(resipipe_bruto, axis=1, ddof=1)

x = np.arange(len(patterns))
width = 0.35

fig, ax = plt.subplots(figsize=(10,6))

bars1 = ax.bar(
    x - width/2,
    openmpi_mean,         
    width,
    yerr=openmpi_std,  
    capsize=8,
    label='OpenMPI',
    facecolor='white',
    edgecolor='#159CEB',
    hatch='////\\\\\\\\',
    linewidth=1.2,
    error_kw=dict(ecolor='#0766F5', linewidth=1.2),
    zorder=3
    )

bars2 = ax.bar(
    x + width/2,
    resipipe_mean,
    width,
    yerr=resipipe_std, 
    capsize=8, 
    label='ResiPipe',
    facecolor='white',
    edgecolor='#F57C25',
    hatch='////\\\\\\\\',
    linewidth=1.2,
    error_kw=dict(ecolor='#F0501A', linewidth=1.2),
    zorder=3
    )


ax.set_xlabel('Aplicação e replicação')
ax.set_ylabel('Throughput (msg/sec)')

ax.set_xticks(x)
ax.set_xticklabels(patterns, rotation=45)

ax.yaxis.grid(True, linestyle=':', linewidth=1)
ax.set_axisbelow(True)

ax.legend(frameon=False)

ax.tick_params(axis='x', labelsize=22)  # aumenta X
ax.tick_params(axis='y', labelsize=22)  # aumenta Y

plt.tight_layout()
plt.savefig("tm.pdf", format="pdf")
plt.show()