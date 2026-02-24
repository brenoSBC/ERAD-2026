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

patterns = ['sa_111', 'sa_121', 'sa_131', 'sa_141', 'sa_161', 'sa_181']

openmpi_bruto = [
    [29658.07122563, 30466.06116660, 28807.51365637],
    [28554.43435903, 28375.64157986, 29011.77148748],
    [11207.68938162, 11274.42535585, 10771.31373085],
    [13512.34258686, 12776.50771670, 13233.58147010],
    [13227.06611419, 14136.04996488, 14200.77124658],
    [13244.79203763, 13599.44607471, 13171.44837169]
]

resipipe_bruto = [
    [26643.23727877, 26096.52823757, 27201.73482818],
    [26281.16512791, 25692.48379926, 25804.54275931],
    [17550.08107974, 18563.05503453, 19013.48961194],
    [15421.56946577, 14094.60400216, 12525.29341509],
    [11729.77209742, 13114.03301788, 11675.28363675],
    [11401.10604196, 9726.70114401, 10652.80628620]
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