"""
Function that creates a random d-regular graph on n vertices.
"""

from collections import defaultdict
from typing import Optional
from dataclasses import dataclass
import random

import numpy as np

from utils import is_regular, is_connected


@dataclass
class S:
    edge_to_weights: dict[tuple[int, int], int]
    degrees: list[int]

    @staticmethod
    def get_S(A: np.array, d: int) -> "S":
        n = len(A)
        edge_to_weights = {}

        degrees = []
        for v in range(n):
            degrees.append(0)

            for u in range(v):
                edge_to_weights[(u, v)] = d*d

        return S(edge_to_weights, degrees)

    def get_pairs(self, indices: np.array, other: int) -> np.array:
        for index in indices:
            index_i = int(index)

            # KeyError happens if one vertex u gets degree d without getting connected to v
            # (hence the edge (u, v) is not in the dictionary)
            # Once v also reaches degree d, we try to remove the edge again
            if other == index_i:
                continue
            if other < index_i:
                if (other, index_i) not in self.edge_to_weights:
                    continue
                yield (other, index_i)
            else:
                if (index_i, other) not in self.edge_to_weights:
                    continue
                yield (index_i, other)

    def delete_from(self, first, indices: np.array) -> None:
        for a, b in self.get_pairs(indices, first):
            self.edge_to_weights.pop((a, b))


    def update_S(self, A: np.array, selected_u: int, selected_v: int, d: int) -> None:
        # We remove the selected edge from the list of options entirely
        self.degrees[selected_u] += 1
        self.degrees[selected_v] += 1

        u_neighbors = np.where(A[selected_u] == 0)[0]
        v_neighbors = np.where(A[selected_v] == 0)[0]

        if self.degrees[selected_u] == d:
            self.delete_from(selected_u, u_neighbors)
        else:
            for a, b in self.get_pairs(u_neighbors, selected_u):
                self.edge_to_weights[(a, b)] = (d - self.degrees[a]) * (d - self.degrees[b])

        if self.degrees[selected_v] == d:
            self.delete_from(selected_v, v_neighbors)
        else:
            for a, b in self.get_pairs(v_neighbors, selected_v):
                self.edge_to_weights[(a, b)] = (d - self.degrees[a]) * (d - self.degrees[b])

        self.edge_to_weights.pop((selected_u, selected_v))

    def is_empty(self) -> bool:
        return len(self.edge_to_weights) == 0

    def get_choices(self) -> tuple[list[tuple[int, int]], list[int]]:
        return list(self.edge_to_weights.keys()), list(self.edge_to_weights.values())


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

            u, v = random.choices(*options.get_choices())[0]
            A[u, v] = 1
            A[v, u] = 1
            options.update_S(A, u, v, d)

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
