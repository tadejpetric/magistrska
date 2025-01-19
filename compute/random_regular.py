"""
Function that creates a random d-regular graph on n vertices.
"""
import logging
from typing import Optional
from dataclasses import dataclass

import numpy as np

from utils import is_ramanujan, is_regular, is_connected


@dataclass
class S:
    probabilities: np.ndarray
    inv_degrees: np.ndarray
    n: int

    @staticmethod
    def get_S(A: np.array, d: int) -> "S":
        n = len(A)

        probabilities = np.full((n,n), d*d, np.int32)
        np.fill_diagonal(probabilities, 0)
        inv_degrees = np.full(n, d, np.int32)

        return S(probabilities, inv_degrees, n)


    def update_S(self, A: np.array, selected_u: int, selected_v: int, d: int) -> None:
        # We remove the selected edge from the list of options entirely
        self.inv_degrees[selected_u] -= 1
        self.inv_degrees[selected_v] -= 1

        assert self.inv_degrees[selected_u] >= 0
        assert self.inv_degrees[selected_v] >= 0

        if self.inv_degrees[selected_u] == 0:
            self.probabilities[:, selected_u] = 0
            self.probabilities[selected_u, :] = 0
        else:
            selected_degree = self.inv_degrees[selected_u]
            mask = self.probabilities[:, selected_u] != 0
            self.probabilities[mask, selected_u] = selected_degree * self.inv_degrees[mask]
            self.probabilities[selected_u, mask] = selected_degree * self.inv_degrees[mask]

        if self.inv_degrees[selected_v] == 0:
            self.probabilities[:, selected_v] = 0
            self.probabilities[selected_v, :] = 0
        else:
            selected_degree = self.inv_degrees[selected_v]
            mask = self.probabilities[:, selected_v] != 0
            self.probabilities[mask, selected_v] = selected_degree * self.inv_degrees[mask]
            self.probabilities[selected_v, mask] = selected_degree * self.inv_degrees[mask]

        self.probabilities[selected_u, selected_v] = 0
        self.probabilities[selected_v, selected_u] = 0

    def to_indices(self, number: int) -> tuple[int, int]:
        return divmod(number, self.n)


def random_regular(n_vertices: int, d: int, max_attempts=10000) -> Optional[np.array]:
    # https://users.monash.edu.au/~nwormald/papers/randgen.pdf
    # Algorithm 2, no reusing S

    A = np.zeros((n_vertices, n_vertices), np.int8)
    rng = np.random.default_rng()

    def attempt() -> np.array:
        A.fill(0)
        options = S.get_S(A, d)

        weights_sum: float = np.sum(options.probabilities.reshape(-1))
        eps = np.finfo(np.float32).eps
        
        while weights_sum > eps:
            u_and_v = rng.choice(options.n*options.n, replace=False, p=options.probabilities.reshape(-1) / weights_sum)
            u, v = options.to_indices(u_and_v)
            while u == v or A[u, v] == 1:
                logging.warning("Somehow chose the same thing, probability: ", options.probabilities[u, v])   
                u_and_v = rng.choice(options.n*options.n, replace=False, p=options.probabilities.reshape(-1) / weights_sum)
                u, v = options.to_indices(u_and_v)

            A[u, v] = 1
            A[v, u] = 1
            options.update_S(A, u, v, d)
            weights_sum = np.sum(options.probabilities.reshape(-1))
        
        return A

    A = attempt()
    nr_attempts = 1

    while not is_regular(A, d) or not is_connected(A):
        if nr_attempts > max_attempts:
            return None
        A = attempt()
        nr_attempts += 1

    return A


def is_random_ramanujan(n_vertices: int, d: int):
    A = random_regular(n_vertices, d)
    if A is None:
        return 0

    return is_ramanujan(A, d)

if __name__ == "__main__":
    A = random_regular(10, 3)
    print(A)
