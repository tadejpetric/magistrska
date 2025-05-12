from hashimoto import hashimoto_matrix

# Random
Srand = """[[0 0 1 1 1 0 0 0 0 1 0 1]
 [0 0 1 0 1 1 0 1 0 0 0 1]
 [1 1 0 0 1 1 0 1 0 0 0 0]
 [1 0 0 0 0 1 0 1 1 0 1 0]
 [1 1 1 0 0 0 0 0 1 0 1 0]
 [0 1 1 1 0 0 1 0 0 0 0 1]
 [0 0 0 0 0 1 0 1 1 1 0 1]
 [0 1 1 1 0 0 1 0 0 1 0 0]
 [0 0 0 1 1 0 1 0 0 1 1 0]
 [1 0 0 0 0 0 1 1 1 0 1 0]
 [0 0 0 1 1 0 0 0 1 1 0 1]
 [1 1 0 0 0 1 1 0 0 0 1 0]]"""


# bottleneck
Sbott = """[[0 1 1 1 1 1 0 0 0 0 0 0]
 [1 0 1 1 1 1 0 0 0 0 0 0]
 [1 1 0 1 1 1 0 0 0 0 0 0]
 [1 1 1 0 1 1 0 0 0 0 0 0]
 [1 1 1 1 0 0 0 1 0 0 0 0]
 [1 1 1 1 0 0 1 0 0 0 0 0]
 [0 0 0 0 0 1 0 0 1 1 1 1]
 [0 0 0 0 1 0 0 0 1 1 1 1]
 [0 0 0 0 0 0 1 1 0 1 1 1]
 [0 0 0 0 0 0 1 1 1 0 1 1]
 [0 0 0 0 0 0 1 1 1 1 0 1]
 [0 0 0 0 0 0 1 1 1 1 1 0]]"""

from numpy_str_to_obj import str_to_obj


import numpy as np

def adjacency_complete_bipartite(n1, n2):
    """
    Returns the adjacency matrix of the complete bipartite graph K_{n1,n2}.
    """
    # top‐left and bottom‐right blocks are zeros
    Z11 = np.zeros((n1, n1), dtype=int)
    Z22 = np.zeros((n2, n2), dtype=int)
    # off‐diagonal blocks are all ones
    J12 = np.ones((n1, n2), dtype=int)
    J21 = np.ones((n2, n1), dtype=int)
    # assemble via np.block
    return np.block([[Z11, J12],
                     [J21, Z22]])

#A = str_to_obj(Srand)
# -> 1, 0.5, 0.25
A = str_to_obj(Sbott)
# -> 1, 0.5, 0.8, 0.31, 0.25
#A = adjacency_complete_bipartite(5,5)
# -> 1, 0.5, 0.25 x2


H = hashimoto_matrix(A)

import numpy as np

evs = 1/np.linalg.eigvals(H)


print("Nontrivial evs have to be", (5-1)**(-1/2))
print("Extremes:", 1/(5-1), "< |l| < ", 1)
print("nr poles", len(evs))
for ev in evs:
    #print(1/ev, ":", 1/np.abs(ev))
    
    print(f"\\fill ({ev.real},{ev.imag}) circle (0.5pt);")
