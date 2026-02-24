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

patterns = ['tm_1111', 'tm_1221', 'tm_1331', 'tm_1441', 'tm_1461', 'tm_1481']

openmpi_bruto = [
    [237.82825224, 238.89546364, 249.67209745],
    [508.18686534, 526.18492365, 501.65408347],
    [744.71599801, 732.47638097, 762.10815956],
    [946.07649300, 928.39561095, 972.17463998],
    [960.80977673, 919.40472661, 928.22674532],
    [939.90347583, 911.44760985, 921.87690983]
]

resipipe_bruto = [
    [261.82594984, 247.96321714, 229.95670193],
    [502.17777279, 523.95863660, 497.57345419],
    [744.81661015, 727.60753266, 755.29846245],
    [975.50270588, 998.51838453, 919.31485908],
    [951.49125263, 924.16751247, 914.67902841],
    [955.19284001, 902.74229892, 921.73419408]
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