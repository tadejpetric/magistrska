"""
Function that creates a random d-regular graph on n vertices.
"""
import logging
from typing import Optional

import numpy as np

from utils import is_ramanujan, is_regular, is_connected


def random_regular(n_vertices: int, d: int, max_attempts=10000) -> Optional[np.array]:
    A = np.zeros((n_vertices, n_vertices), np.int8)
    rng = np.random.default_rng()

    # For every edge, pick d random vertices and assign them as neighbors
    def attempt() -> np.array:
        A.fill(0)
        
        inv_degrees = np.full(n_vertices, d, np.int32)

        for u in range(n_vertices):
            while inv_degrees[u] > 0:
                selected = rng.choice(n_vertices, replace=False, shuffle=False, size=inv_degrees[u])
                for v in selected:
                    if u == v or inv_degrees[v] == 0:
                        continue
                    if A[u, v] == 1:
                        continue
                    A[u, v] = 1
                    A[v, u] = 1
                    inv_degrees[u] -= 1
                    inv_degrees[v] -= 1
                
                # if 1-A has 0 element it's already connected (hence unavailable)
                # if inv has a 0 element, that degree is already reached (hence unavailable)
                
                if inv_degrees[u] == 0:
                    continue
                valid = (1-A[u,:]) * inv_degrees
                valid[u] = 0
                if np.sum(valid) == 0:
                    return A
        
        return A

    A = attempt()
    nr_attempts = 1

    while not is_regular(A, d) or not is_connected(A):
        if nr_attempts > max_attempts:
            return None
        A = attempt()
        nr_attempts += 1

    return A


if __name__ == "__main__":
    A = random_regular(10, 3)
    print(A)

def is_random_ramanujan(n_vertices: int, d: int):
    A = random_regular(n_vertices, d)
    if A is None:
        return 0

    return is_ramanujan(A, d)