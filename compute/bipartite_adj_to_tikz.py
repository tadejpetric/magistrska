import numpy as np
from collections import deque

def compute_bipartite_partition(adj):
    """
    Computes the bipartite partition of a connected graph represented by an adjacency matrix.
    Assumes the graph is bipartite.
    
    Parameters:
        adj (np.ndarray): A square numpy array representing the adjacency matrix.
        
    Returns:
        list: A list 'partition' where partition[i] is 0 or 1 indicating the group of vertex i.
    """
    n = adj.shape[0]
    partition = [-1] * n
    queue = deque([0])
    partition[0] = 0  # start by putting vertex 0 in partition 0
    
    while queue:
        u = queue.popleft()
        for v, connected in enumerate(adj[u]):
            if connected:
                if partition[v] == -1:
                    partition[v] = 1 - partition[u]  # alternate partition
                    queue.append(v)
                elif partition[v] == partition[u]:
                    raise ValueError("Graph is not bipartite")
    return partition

def generate_tikz(adj):
    """
    Generates TikZ code for a bipartite graph.
    
    This function computes the bipartite partition automatically. It then places vertices
    from one partition along the left column (x=0) and vertices from the other partition along
    the right column (x=3), with y‑positions chosen so that they are vertically centered.
    
    Parameters:
        adj (np.ndarray): A square numpy array representing the adjacency matrix.
    
    Returns:
        str: A string containing the TikZ code.
    """
    partition = compute_bipartite_partition(adj)
    
    # Separate vertices by partition
    left_vertices = [v for v in range(len(partition)) if partition[v] == 0]
    right_vertices = [v for v in range(len(partition)) if partition[v] == 1]
    
    # Check that the partitions are of equal size (as stated in the problem)
    if len(left_vertices) != len(right_vertices):
        raise ValueError("The two partitions do not have an equal number of vertices.")
    
    tikz_code = "\\begin{figure}[H]\n\\centering\n"
    tikz_code += "\\begin{tikzpicture}[scale=1, transform shape]\n"
    
    # Place left vertices at x=0
    n_left = len(left_vertices)
    offset_left = (n_left - 1) / 2.0  # center the vertices vertically
    left_positions = {}
    for i, v in enumerate(left_vertices):
        y = offset_left - i
        tikz_code += f"  \\node[circle, fill=black, inner sep=2pt] (L{i}) at ({y}, 0) {{}};\n"
        left_positions[v] = f"L{i}"
    
    # Place right vertices at x=3
    n_right = len(right_vertices)
    offset_right = (n_right - 1) / 2.0
    right_positions = {}
    for i, v in enumerate(right_vertices):
        y = offset_right - i
        tikz_code += f"  \\node[circle, fill=black, inner sep=2pt] (R{i}) at ({y}, 3) {{}};\n"
        right_positions[v] = f"R{i}"
    
    # Draw each edge once.
    # Since the graph is undirected, we iterate over each pair (u,v) with u < v.
    for u in range(len(partition)):
        for v in range(u+1, len(partition)):
            if adj[u, v]:
                # Determine which vertex is in which partition
                if partition[u] == 0 and partition[v] == 1:
                    tikz_code += f"  \\draw ({left_positions[u]}) -- ({right_positions[v]});\n"
                elif partition[u] == 1 and partition[v] == 0:
                    tikz_code += f"  \\draw ({left_positions[v]}) -- ({right_positions[u]});\n"
                else:
                    # This case should not occur in a bipartite graph.
                    pass
                    
    tikz_code += "\\end{tikzpicture}\n"
    tikz_code += "\\end{figure}\n"
    return tikz_code

if __name__ == '__main__':
    # Example adjacency matrix for a bipartite graph with 4 vertices.
    # This matrix connects vertices 0 and 1 with vertices 2 and 3.
    adj = np.array([[0, 0, 1, 1],
                    [0, 0, 1, 1],
                    [1, 1, 0, 0],
                    [1, 1, 0, 0]])
    
    tikz_output = generate_tikz(adj)
    print(tikz_output)
