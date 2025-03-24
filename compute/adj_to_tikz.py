import numpy as np


def adjacency_to_tikz(adj_matrix, radius=2):
    """
    Transforms a directed, unweighted graph's adjacency matrix into a LaTeX/TikZ graph.

    Parameters:
        adj_matrix (np.ndarray): A square numpy array representing the adjacency matrix.
        radius (float): The radius of the circle on which nodes will be placed.

    Returns:
        str: A string containing LaTeX code that draws the graph using TikZ.
    """
    n = adj_matrix.shape[0]
    # Start the LaTeX string with a center environment and the tikzpicture
    tikz_str = "\\begin{center}\n    \\begin{tikzpicture}\n"

    # Place each node on the circle
    for i in range(n):
        # Label nodes as A, B, C, ... (assumes n <= 26)
        node_label = chr(65 + i)
        # Calculate the angle (in degrees) for the node's position
        angle = 360 / n * i
        tikz_str += f"        \\node[circle, fill=black, inner sep=2pt] ({node_label}) at ({angle}: {radius}) {{}};\n"

    # Add directed edges (using [->]) where the matrix has a non-zero entry.
    for i in range(n):
        for j in range(i):
            if adj_matrix[i, j] != 0:
                from_node = chr(65 + i)
                to_node = chr(65 + j)
                tikz_str += f"        \\draw ({from_node}) -- ({to_node});\n"

    # End the tikzpicture and center environment
    tikz_str += "    \\end{tikzpicture}\n\\end{center}"
    return tikz_str


# Example usage:
if __name__ == "__main__":
    from random_regular_networkx import random_regular

    before = np.array(
        [
            [0, 1, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1],
            [0, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 0, 0],
        ]
    )
    #print(adjacency_to_tikz(before))
    n = 12
    d = 5

    rg = random_regular(n, d)
    
    latex_code = adjacency_to_tikz(rg)
    #
    from utils import second_eigenvalue, is_ramanujan, spectral_gap
    import math
    from cheeger import cheeger
    print(rg)
    print("To be ramanujan, ev under", 2*math.sqrt(d-1))
    print("Spectral gap", spectral_gap(rg))
    print("Eigenvalue:", second_eigenvalue(rg))
    print("Is ramanujan: ", is_ramanujan(rg))
    print("Cheeger:", cheeger(rg))
    print(latex_code)
