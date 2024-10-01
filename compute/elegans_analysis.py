import numpy as np


data_path = "/home/tadej/magistrska/compute/C-elegans-frontal.txt"

node_cnt = 131

adj_matrix = np.zeros((node_cnt, node_cnt), dtype=np.int8)


with open(data_path) as fh:
    for line in fh:
        if line.startswith("#"):
            continue
        left, right = map(int, line.split())

        assert left != right
        adj_matrix[left, right] = 1
        adj_matrix[right, left] = 1

print(f"Num nodes: {node_cnt}")
print("Num edges: 764")

# Get highest degree of a vertex
max_degree = np.max(np.sum(adj_matrix, axis=1))
print(f"Max degree: {max_degree}")

# Get average degree of a vertex
avg_degree = np.mean(np.sum(adj_matrix, axis=1))
print(f"Avg degree: {avg_degree}")

# Get lowest degree of a vertex
min_degree = np.min(np.sum(adj_matrix, axis=1))
print(f"Min degree: {min_degree}")

# 5 highest eigenvalues
eigenvalues = sorted(np.linalg.eigvals(adj_matrix))
print(f"5 highest eigenvalues: {eigenvalues[-5:]}")

# 5 lowest eigenvalues
print(f"5 lowest eigenvalues: {eigenvalues[:5]}")

# Spectral gap
print(f"Spectral gap: {eigenvalues[-1] - eigenvalues[-2]}")

# Gap is only ~4.17
# There is an article backing that up: https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1007526

