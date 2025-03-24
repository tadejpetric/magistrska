import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def display_graph(adj_matrix):
    """
    Displays a graph from the given adjacency matrix.
    
    Parameters:
    adj_matrix (list of list or numpy array): The adjacency matrix of the graph.
    """
    # Convert adjacency matrix to a NumPy array
    adj_matrix = np.array(adj_matrix)

    # Create a directed/undirected graph based on the adjacency matrix
    G = nx.Graph() if np.array_equal(adj_matrix, adj_matrix.T) else nx.DiGraph()

    # Add nodes
    num_nodes = adj_matrix.shape[0]
    G.add_nodes_from(range(num_nodes))

    # Add edges
    for i in range(num_nodes):
        for j in range(num_nodes):
            if adj_matrix[i][j] != 0:  # Non-zero means an edge exists
                G.add_edge(i, j, weight=adj_matrix[i][j])

    # Draw the graph
    pos = nx.spring_layout(G)  # Layout for visualization
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=12)
    
    # Draw edge labels if weights are present
    labels = {(i, j): adj_matrix[i][j] for i in range(num_nodes) for j in range(num_nodes) if adj_matrix[i][j] != 0}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Show the graph
    plt.show()


