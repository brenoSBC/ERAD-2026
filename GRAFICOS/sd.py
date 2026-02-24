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

patterns = ['sd_1111', 'sd_1221', 'sd_1331', 'sd_1441', 'sd_1461', 'sd_1481']

openmpi_bruto = [
    [13129.62281082, 13200.66682347, 13401.47064265],
    [10262.01107746, 10446.68412110, 10279.87413022],
    [10384.08624693, 10366.86498691, 11255.45450551],
    [8005.33171396, 8539.37458194, 7969.93225416],
    [7960.05839825, 7626.74586130, 8311.01366892],
    [7131.54195910, 7620.17822636, 7017.88256756]
]

resipipe_bruto = [
    [11731.10368606, 11982.84244108, 12492.19655783],
    [8495.78269869, 9000.49561199, 9704.74439181],
    [8295.69965982, 8578.64882240, 9574.11009376],
    [7330.78358132, 7258.87758153, 7854.79609481],
    [7617.71172119, 6942.78608153, 6944.34687687],
    [6673.33473175, 6267.44275376, 6598.25072846]
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