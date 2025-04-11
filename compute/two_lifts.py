import numpy as np
import itertools
from bipartite_adj_to_tikz import generate_tikz


def generate_2lifts(adj_matrix):
    """
    Given an n x n adjacency matrix for an undirected graph G,
    yields the 2n x 2n adjacency matrix for every 2-lift of G.
    
    Each edge (u, v) in G (with u < v) gives a binary choice:
      - Choice 0: add edges (u, v) and (u+n, v+n)
      - Choice 1: add edges (u, v+n) and (u+n, v)
    
    Parameters:
        adj_matrix (np.ndarray): An n x n symmetric numpy array.
    
    Yields:
        np.ndarray: A 2n x 2n numpy array representing a 2-lift of G.
    """
    n = adj_matrix.shape[0]
    # Extract undirected edges (u, v) with u < v and a non-zero entry.
    edges = [(u, v) for u in range(n) for v in range(u+1, n) if adj_matrix[u, v] != 0]

    # Iterate over all possible choices (0 or 1 for each edge).
    for choices in itertools.product([0, 1], repeat=len(edges)):
        # Initialize the 2n x 2n adjacency matrix with zeros.
        lift_adj = np.zeros((2*n, 2*n), dtype=int)
        
        # Process each edge with its corresponding choice.
        for (choice, (u, v)) in zip(choices, edges):
            if choice == 0:
                # First type: parallel edges.
                # Connect iota_1(u) with iota_1(v)
                lift_adj[u, v] = 1
                lift_adj[v, u] = 1
                # Connect iota_2(u) with iota_2(v)
                lift_adj[u+n, v+n] = 1
                lift_adj[v+n, u+n] = 1
            else:
                # Second type: crossed edges.
                # Connect iota_1(u) with iota_2(v)
                lift_adj[u, v+n] = 1
                lift_adj[v+n, u] = 1
                # Connect iota_2(u) with iota_1(v)
                lift_adj[u+n, v] = 1
                lift_adj[v, u+n] = 1

        yield lift_adj

# Example usage:

from utils import is_connected
from utils import is_ramanujan
if __name__ == "__main__":
    # Define a simple graph K55
    n = 3
    A = np.zeros((2*n, 2*n), dtype=int)

    # Connect every vertex in the first partition (vertices 0 to 4)
    # to every vertex in the second partition (vertices 5 to 9)
    A[:n, n:] = 1
    A[n:, :n] = 1
    
    print("Original graph adjacency matrix:")
    print(A)
    print(generate_tikz(A))
    
    print("\n2-lifts of the graph:")
    swap = True
    while True:
        if swap:
            iterator = generate_2lifts(A)
        # Find a connected graph
        while True:
            lift = next(iterator)
            if is_connected(lift):
                break
        
        print(lift)
        print(generate_tikz(lift))
        print("size:", len(lift))
        print("is ramanujan:", is_ramanujan(lift))
        
        A = lift
        x = input("swap?")
        if x == "y":
            swap = True
        else:
            swap = False 
        
