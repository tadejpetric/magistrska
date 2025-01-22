from networkx import random_regular_graph, to_numpy_array, is_regular_expander
from utils import is_ramanujan, is_ramanujan_simp
import numpy as np
def random_regular(n_vertices: int, d: int):
    G = random_regular_graph(d, n_vertices)
    return to_numpy_array(G)

def is_random_ramanujan(n_vertices: int, d: int):
    # https://github.com/networkx/networkx/blob/ba6744c1dc432c7beea0210584f16b80761c5fda/networkx/generators/expanders.py
    # /home/user/sola/magistrska/.venv/lib/python3.13/site-packages/networkx/generators/expanders.py
    # Has a bug in line 399, not merged yet. change ** -> *
    G = random_regular_graph(d, n_vertices)
    return is_regular_expander(G)

def is_random_ramanujan_eps(n_vertices: int, d: int, eps: float):
    # https://github.com/networkx/networkx/blob/ba6744c1dc432c7beea0210584f16b80761c5fda/networkx/generators/expanders.py
    # Has a bug in line 399, not merged yet. change ** -> *
    G = random_regular_graph(d, n_vertices)
    return is_regular_expander(G, epsilon=eps)