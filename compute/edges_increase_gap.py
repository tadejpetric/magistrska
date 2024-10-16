import numpy as np

import networkx as nx
import matplotlib.pyplot as plt

    
num_vertices = 6
edges_to_remove = 10

def graph_is_connected(adj_matrix: np.array) -> bool:
    visible = [False] * len(adj_matrix)

    # Add edges visible from the first vertex
    visible[0] = True
    for idx, has_edge in enumerate(adj_matrix[0]):
        if has_edge:
            visible[idx] = True
    
    changed_something = True

    while changed_something:
        changed_something = False
        for i, visited in enumerate(visible):
            if visited:
                for idx, has_edge in enumerate(adj_matrix[i]):
                    if has_edge and not visible[idx]:
                        visible[idx] = True
                        changed_something = True
    
    return all(visible)

np.random.seed(0)

# Start with a fully-connected graph
adj_matrix = np.ones((num_vertices, num_vertices), dtype=np.int8)

for i in range(num_vertices):
    adj_matrix[i, i] = 0

def spectral_gap(matrix: np.array):
    eigenvalues = sorted(np.linalg.eigvals(matrix).real)
    return eigenvalues[-1] - eigenvalues[-2]

gap = spectral_gap(adj_matrix)
print(f"Initial gap: {gap}")

for _ in range(edges_to_remove):
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                continue
            if adj_matrix[i, j] == 1:
                adj_matrix_copy = adj_matrix.copy()
                adj_matrix_copy[i, j] = 0
                adj_matrix_copy[j, i] = 0
                if not graph_is_connected(adj_matrix_copy):
                    continue
                new_gap = spectral_gap(adj_matrix_copy)

                if new_gap > gap:
                    print(f"Started with gap {gap}, got new gap {new_gap}")
                    print(adj_matrix)

                    print(adj_matrix_copy)
                    raise Exception("end")
                else:
                    print(f"Smaller new gap {new_gap}")
                
    while True:
        i, j = np.random.randint(0, num_vertices, 2)
        if i == j:
            continue
        if adj_matrix[i, j] == 1:
            adj_matrix[i, j] = 0
            adj_matrix[j, i] = 0
            break
    
    gap = spectral_gap(adj_matrix)
    print(f"Removed edge, new gap: {gap}")