import numpy as np

def hashimoto_matrix(adj: np.ndarray, return_edge_index=False):
    """
    Build the (non-backtracking) Hashimoto matrix H for a graph.

    Parameters
    ----------
    adj : np.ndarray
        Square 0/1 adjacency matrix of the graph (shape n x n).
        • adj[i, j] = 1  ⇔  edge i-j is present.
        • Both undirected and directed graphs are allowed.
          For undirected graphs the matrix should be symmetric.
    return_edge_index : bool, default=False
        If True, also return the list that maps row/column indices
        of H to the corresponding directed edge (tail, head).

    Returns
    -------
    H : np.ndarray
        The m x m Hashimoto matrix, where m is the number of directed
        edges (for an undirected graph, m = 2⋅|E|).
    edge_index : list[tuple[int, int]]
        Only returned when `return_edge_index=True`.
        `edge_index[k] = (u, v)` means row/column k of H
        corresponds to the directed edge u→v.
    """
    n = adj.shape[0]
    if adj.shape[1] != n:
        raise ValueError("Adjacency matrix must be square.")
    
    # Enumerate all directed edges. Represents rows / columns
    edge_index = [(u, v)
                  for u in range(n)
                  for v in range(n)
                  if adj[u, v]]
    m = len(edge_index)

    H = np.zeros((m, m), dtype=int)
    # Iterate over all edges
    for i, (u, v) in enumerate(edge_index):
        for j, (up, vp) in enumerate(edge_index):
            if v == up and u != vp:
                H[i, j] = 1

    return (H, edge_index) if return_edge_index else H


if __name__ == "__main__":
    A = np.array([[0,1,1],[1,0,1],[1,1,0]])
    H = hashimoto_matrix(A)
    print(H)

