import numpy as np
from pgl_utils import lps_generators

# Assumes get_gens(q, p) -> list of numpy.ndarray 2x2 matrices over GF(q)
# Generates the adjacency matrix of the Cayley graph of PGL(2, q) with given generators.

def adjacency_matrix(q, p):
    """
    Return the adjacency matrix (as a numpy.matrix) of the Cayley graph of PGL(2, q)
    with the p+1 generators returned by get_gens(q, p).

    Parameters:
    q (int): prime modulus for the field GF(q).
    p (int): such that there are p+1 generators.

    Returns:
    A (numpy.matrix): adjacency matrix of size n x n, where n = q*(q**2 - 1).
    """
    # Retrieve generators
    gens = lps_generators(q, p)

    # Normalize a matrix to a canonical projective representative
    def normalize(M):
        M = M % q
        # Find first nonzero entry and scale so that entry = 1
        for i in range(2):
            for j in range(2):
                e = int(M[i, j])
                if e != 0:
                    inv = pow(e, q-2, q)  # modular inverse since q is prime
                    return (M * inv) % q
        return M

    # Enumerate group elements via BFS
    G = []                        # list of matrices
    G_index = {}                  # map flattened tuple -> index
    I = np.eye(2, dtype=int)
    G.append(I)
    G_index[tuple(I.flatten())] = 0
    queue = [I]

    while queue:
        curr = queue.pop(0)
        for s in gens:
            nxt = np.mod(curr.dot(s), q)
            nxt = normalize(nxt)
            key = tuple(nxt.flatten())
            if key not in G_index:
                G_index[key] = len(G)
                G.append(nxt)
                queue.append(nxt)

    n = len(G)
    # Initialize adjacency matrix
    A = np.zeros((n, n), dtype=int)

    # Fill adjacency
    for i, g in enumerate(G):
        for s in gens:
            h = np.mod(g.dot(s), q)
            h = normalize(h)
            j = G_index[tuple(h.flatten())]
            A[i, j] = 1

    return np.matrix(A)


adjacency_matrix()