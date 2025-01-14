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
    degrees: list[int]

    @staticmethod
    def get_S(A: np.array, d: int) -> "S":
        n = len(A)
        edge_options = []
        weights = []

        degrees = []
        for v in range(n):
            degrees.append(0)

            for u in range(v):
                edge_options.append((u, v))
                weights.append(d*d)

        return S(edge_options, weights, degrees)
    
    def update_S(self, selected_u:int, selected_v:int, d:int) -> None:
        # We remove the selected edge from the list of options entirely
        self.degrees[selected_u] += 1
        self.degrees[selected_v] += 1

        new_weights = []
        new_edge_options = []
        for u, v in self.edge_options:
            if u == selected_u and v == selected_v:
                continue
            
            if self.degrees[u] == d or self.degrees[v] == d:
                continue

            new_weights.append((d - self.degrees[v]) * (d - self.degrees[u]))
            new_edge_options.append((u, v))
        
        self.weights = new_weights
        self.edge_options = new_edge_options

    def is_empty(self) -> bool:
        return len(self.edge_options) == 0



def random_regular(n_vertices: int, d: int, max_attempts=10000) -> Optional[np.array]:
    # https://users.monash.edu.au/~nwormald/papers/randgen.pdf
    # Algorithm 2, no reusing S

    A = np.zeros((n_vertices, n_vertices), np.int8)
    def attempt() -> np.array:
        A.fill(0)
        options = S.get_S(A, d)

        while True:
            if options.is_empty():
                return A

            u, v = random.choices(options.edge_options, options.weights)[0]
            A[u, v] = 1
            A[v, u] = 1
            options.update_S(u, v, d)

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