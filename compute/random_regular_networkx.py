from networkx import random_regular_graph, to_numpy_array, is_regular_expander

def random_regular(n_vertices: int, d: int):
    G = random_regular_graph(d, n_vertices)
    return to_numpy_array(G)

def is_random_ramanujan(n_vertices: int, d: int):
    G = random_regular_graph(d, n_vertices)
    return is_regular_expander(G)

def is_random_ramanujan_eps(n_vertices: int, d: int, eps: float):
    G = random_regular_graph(d, n_vertices)
    return is_regular_expander(G, epsilon=eps)