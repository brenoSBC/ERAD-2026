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

openmpi = [10028.19, 756.80, 1694.60, 1004.12, 1235.88, 1125.69]
resipipe = [6477.66, 2457.30, 2338.62, 3204, 3542.61, 2920.44]

overhead = [
    (o - r) / o * 100
    for o, r in zip(openmpi, resipipe)
]

x = np.arange(len(patterns))
width = 0.35

fig, ax = plt.subplots(figsize=(10,6))

# ---- Barras com hachura ----
bars1 = ax.bar(
    x - width/2,
    openmpi,
    width,
    label='OpenMPI',
    facecolor='white',
    edgecolor='#00B3FF',
    hatch='//////\\\\\\\\\\\\\\\\',
    linewidth=1.2
)

bars2 = ax.bar(
    x + width/2,
    resipipe,
    width,
    label='ResiPipe',
    facecolor='white',
    edgecolor='#FF8800',
    hatch='//////\\\\\\\\\\\\\\\\',
    linewidth=1.2
)

# Eixo secundário
ax2 = ax.twinx()

ax2.plot(
    x,
    overhead,
    color='black',
    marker='o',
    linestyle='-',
    linewidth=2,
    label='ResiPipe Overhead (%)'
)

ax2.set_ylabel('Diferença relativa')
ax2.set_ylim(0, max(overhead)*1.3)

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