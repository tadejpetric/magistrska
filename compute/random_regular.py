"""
Function that creates a random d-regular graph on n vertices.
"""

from typing import Optional
from dataclasses import dataclass
import random

import numpy as np

from utils import is_regular, is_connected


@dataclass
class S:
    edge_options: list[tuple[int, int]]
    weights: list[float]

    @staticmethod
    def get_S(A: np.array, d: int) -> "S":
        n = len(A)
        edge_options = []
        weights = []

        degrees = []
        for v in range(n):
            degrees.append(np.sum(A[v]))

            # Select only vertices that need more edges
            if degrees[-1] == d:
                continue
            for u in range(v):
                # Don't add edges to adjacent vertices
                if A[u, v] == 1:
                    continue
                edge_options.append((u, v))
                weights.append((d - degrees[u]) * (d - degrees[v]))

        return S(edge_options, weights)

    def is_empty(self) -> bool:
        return len(self.edge_options) == 0
    
    def zero_weights(self) -> bool:
        return all(w < np.finfo(np.float32).eps for w in self.weights)


def random_regular(n_vertices: int, d: int, max_attempts=10000) -> Optional[np.array]:
    # https://users.monash.edu.au/~nwormald/papers/randgen.pdf
    # Algorithm 2, no reusing S

    def attempt() -> np.array:
        A = np.zeros((n_vertices, n_vertices), np.int8)

        while True:
            options = S.get_S(A, d)

            if options.is_empty():
                return A

            # All weights can be zero if all the neighbors of a vertex already have degree d
            # The graph will not be regular, so another attempt will be made.
            if options.zero_weights():
                return A

            u, v = random.choices(options.edge_options, options.weights)[0]
            A[u, v] = 1
            A[v, u] = 1

    A = attempt()
    nr_attempts = 1

    while not is_regular(A, d) or not is_connected(A):
        if nr_attempts > max_attempts:
            return None
        A = attempt()
        nr_attempts += 1

    return A
