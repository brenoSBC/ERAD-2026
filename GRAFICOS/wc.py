import matplotlib.pyplot as plt
import numpy as np

# ---- Estilo geral parecido com artigo científico ----
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 14,
    "axes.labelsize": 18,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    "legend.fontsize": 14,
    "axes.linewidth": 1.2
})

patterns = ['wc_1111', 'wc_1221', 'wc_1331', 'wc_1441', 'wc_1461', 'wc_1481']

openmpi_bruto = [
    [9486.64176398, 10278.24357427, 10321.67907808],
    [766.53578839, 751.41612114, 750.44707826],
    [1658.07634811, 1710.48111977, 1715.24388259],
    [1001.61910609, 1004.35328446, 1006.39394847],
    [1204.09754956, 1235.74310840, 1265.80932819],
    [1133.53116004, 1108.55922866, 1134.99132414]
]

resipipe_bruto = [
    [6100.96927695, 6759.45526657, 6572.57049246],
    [2353.27680497, 2555.58735121, 2465.02814687],
    [2395.86539520, 2334.48364285, 2285.48663472],
    [3153.17550849, 3250.05162654, 3210.77484164],
    [3765.30273215, 3376.41291329, 3486.11080730],
    [2885.52251018, 2948.97675787, 2926.79771990]
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
    edgecolor='#00B3FF',
    hatch='//////\\\\\\\\\\\\\\\\',
    linewidth=1.2,
    error_kw=dict(ecolor='#00B3FF', linewidth=1.2),
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
    edgecolor='#FF8800',
    hatch='//////\\\\\\\\\\\\\\\\',
    linewidth=1.2,
    error_kw=dict(ecolor='#FF8800', linewidth=1.2),
    zorder=3
    )


# ---- Labels ----
ax.set_xlabel('Aplicação e replicação')
ax.set_ylabel('Throughput (msg/sec)')

ax.set_xticks(x)
ax.set_xticklabels(patterns, rotation=45)

# ---- Grid pontilhado horizontal ----
ax.yaxis.grid(True, linestyle=':', linewidth=1)
ax.set_axisbelow(True)

# ---- Legenda estilo limpo ----
ax.legend(frameon=False)

plt.tight_layout()
plt.show()