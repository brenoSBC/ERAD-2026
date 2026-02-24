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

patterns = ['fd_111', 'fd_121', 'fd_131', 'fd_141', 'fd_161', 'fd_181']

openmpi_bruto = [
    [70980.35986764, 73462.93184659, 71691.12264383], #111
    [69842.81988230, 77914.70330006, 70678.16605777], #121
    [62389.99350396, 64754.73663544, 66037.12893854], #131
    [17564.08174091, 16224.08750323, 17567.67965614], #141
    [14011.61195927, 13792.07193251, 13408.48167730], #161
    [12659.07229250, 12914.33458727, 12976.59267487]  #181
]

resipipe_bruto = [
    [60339.49602433, 59409.70323743, 61366.42398335],
    [62156.52471175, 57750.91929601, 59906.06076081],
    [36687.10583374, 36560.08947162, 36070.26537484],
    [14866.87385418, 14459.67461128, 15621.44508131],
    [11823.09941761, 12300.86138758, 12370.51640773],
    [11459.25006403, 11335.15656275, 11407.22264512]
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