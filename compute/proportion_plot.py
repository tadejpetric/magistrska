from utils import second_eigenvalue
from random_regular_networkx import random_regular

from tqdm import tqdm
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import bisect

d = 5
start_vertices = 20
end_vertices   = 1000
vertex_step    = 4

min_c = -0.5
max_c = .2
c_step = 0.001

attempts_per_size = 1000       

n_values = list(range(start_vertices, end_vertices + 1, vertex_step))
c_values = np.arange(min_c, max_c + 1e-9, c_step)

eigenvals = []
for n in tqdm(n_values):
    second_eigenvals = []
    
    for _attempt in range(attempts_per_size):
        A = random_regular(n, d)
        second_eigenvals.append(second_eigenvalue(A, d))
    
    second_eigenvals.sort()
    eigenvals.append(second_eigenvals)

print("Eigenvalues precomputed")

# proportions[c_index, n_index] = proportion of graphs whose second eigenvalue 
#                                 exceeds 2*sqrt(d-1) + c
proportions = np.zeros((len(c_values), len(n_values)))

for i, second_eigenvals in enumerate(eigenvals):
    n = n_values[i]

    # Could do in O(n) instead of O(n log(n)) but it doesn't matter
    for j, c in enumerate(c_values):
        threshold = 2.0 * np.sqrt(d - 1) + c
        idx = bisect.bisect_right(second_eigenvals, threshold)
        count_exceed = attempts_per_size - idx

        proportions[j, i] = count_exceed / attempts_per_size

np.save('proportions.npy', proportions)
#proportions = np.load('proportions.npy') # uncomment if needed

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

# \printinunitsof{in}\prntlen{\textwidth}
plt.figure(figsize=(5.90666, 6))

plt.imshow(
    proportions, 
    origin='lower',
    extent=[start_vertices, end_vertices, min_c, max_c],
    aspect='auto',
    vmin=0, vmax=1,   # proportion is between 0 and 1
    cmap='binary'
)

plt.axhline(y=0, color='dodgerblue', linestyle='--', linewidth=1.5)

plt.colorbar(label='delež $\\lambda_2 > 2\\sqrt{d-1} + c$')
plt.xlabel('Število vozlišč')
plt.ylabel('c')

n_tick_cnt = 5
c_tick_cnt = 8

n_ticks = np.linspace(start_vertices, end_vertices, n_tick_cnt)
c_ticks = np.linspace(min_c, max_c, c_tick_cnt)
plt.xticks(n_ticks)
plt.yticks(c_ticks)

#plt.title(f'Delež ${d}$-regularnih grafov z ' +
          #r'$\lambda_2 > 2\sqrt{d-1} + c$')
plt.tight_layout()
plt.savefig('/home/user/sola/magistrska/article/images/proportion_plot.pgf')
# change proportion_plot -> images/proportion_plot in the .pgf file


