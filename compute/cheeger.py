from typing import Iterable
import numpy as np


def boundary(A: np.array, S: list[int]) -> int:
    # computes the |d S| of the adjacency matrix A
    vert_set = set(S)
    counter = 0
    for vert in S:
        row = A[vert]
        # find all neighbours of every element of S
        (neighbours,) = np.where(row == 1)

        # If those neighbours aren't in S, it's in dS
        counter += len(set(neighbours) - vert_set)

    return counter


def num_to_S(n: int) -> list[int]:
    indicators = map(int, reversed(bin(n)[2:]))
    S = []
    for idx, is_in in enumerate(indicators):
        if is_in:
            S.append(idx)
    return S


def subset_iterator(vertices: int) -> Iterable[list[int]]:
    # Iterates over all subsets of vertices, with the subset
    # having <= n/2 vertices

    # We use the binary representation of a number
    # a vertex-digit binary number has 1 on index i if
    # vertex i is in S
    n = 1
    while n < 2**vertices:
        S = num_to_S(n)
        if 2 * len(S) <= vertices:
            yield S
        n += 1


def cheeger(A: np.array) -> float:
    # computes the min(|dS| / S)
    current_best = float("inf")
    best_S = None

    for S in subset_iterator(len(A)):
        dS = boundary(A, S)
        cheeger_value = dS / len(S)

        if cheeger_value < current_best:
            best_S = S
            current_best = cheeger_value

    print(best_S)
    return current_best


C_4 = np.array(
    [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
    ]
)
C_6 = np.array(
    [
        [0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0],
    ]
)
K_5 = np.array(
    [
        [0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
    ]
)

# print(cheeger(K_5))

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

after = np.array(
    [
        [0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [0, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0, 0],
    ]
)
from utils import second_eigenvalue, spectral_gap

print("before", cheeger(before), spectral_gap(before))
print("after", cheeger(after), spectral_gap(after))

"""
[[0 1 1 1 1 0 1 1 1]
 [1 0 1 1 1 1 1 1 0]
 [1 1 0 1 1 0 1 1 1]
 [1 1 1 0 1 1 1 0 1]
 [1 1 1 1 0 1 1 0 1]
 [0 1 0 1 1 0 1 1 1]
 [1 1 1 1 1 1 0 0 0]
 [1 1 1 0 0 1 0 0 0]
 [1 0 1 1 1 1 0 0 0]]
[[0 1 1 1 1 0 1 1 1]
 [1 0 1 1 1 1 1 1 0]
 [1 1 0 1 1 0 1 1 1]
 [1 1 1 0 1 1 1 0 1]
 [1 1 1 1 0 1 1 0 0]
 [0 1 0 1 1 0 1 1 1]
 [1 1 1 1 1 1 0 0 0]
 [1 1 1 0 0 1 0 0 0]
 [1 0 1 1 0 1 0 0 0]]
 """

from definicije_spectral_gap_bottleneck import one_connection
print(cheeger(one_connection(6)))
print(second_eigenvalue(one_connection(6)), "<----")
# print(bottleneck)
# print(cheeger(bottleneck))

# from display_graph import display_graph

# display_graph(bottleneck)


# has 2nd eigenvalue 2.48, is ramanujan (under 3.46)
random_graph = np.array(
    [
        [0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
    ]
)

# print(cheeger(random_graph))
from adj_to_tikz import adjacency_to_tikz
print(adjacency_to_tikz(random_graph))