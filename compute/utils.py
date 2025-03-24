from typing import Optional
import logging
import math

import numpy as np


def is_regular(A: np.array, d: Optional[int] = None) -> bool:
    if d is None:
        d = np.sum(A[0])
    for row in A:
        if np.sum(row) != d:
            return False
    return True


def is_connected(A: np.array) -> bool:
    n = len(A)
    visited = [False] * n

    queue = [0]

    while len(queue) > 0:
        v = queue.pop()
        visited[v] = True
        (neighbours,) = np.where(A[v] == 1)
        for u in neighbours:
            if not visited[u]:
                queue.append(u)

    return all(visited)


def is_ramanujan(A: np.array, d: Optional[int] = None) -> bool:
    # We do not verify that A is regular

    evals = sorted(map(lambda x: abs(x), np.linalg.eigvalsh(A)))
    if d is None:
        d = round(evals[-1])

    cntr = 0
    for ev in reversed(evals):
        # Find all eigenvalues that are roughly d
        if ev > d - 0.001:
            cntr += 1
            continue
        if cntr == 0:
            logging.warn("Irregular graph given")
        if cntr == 2:
            logging.info("Bipartite graph given")
        if cntr > 2:
            logging.warning("Disconnected graph given")

        # Check if the next eigenvalue (first nontrivial one) is within the bounds
        return ev <= 2 * math.sqrt(d - 1)

def is_ramanujan_simp(A: np.array, d: Optional[int] = None) -> bool:
    sorted_ev = sorted(np.linalg.eigvalsh(A))
    second_ev = max(abs(sorted_ev[-2]), abs(sorted_ev[0]))
    if d is None:
        d = round(sorted_ev[-1])
    return second_ev <= 2 * math.sqrt(d - 1)

def second_eigenvalue(A: np.array, d: Optional[int] = None) -> float:
    # Works on regular graphs
    evals = sorted(map(lambda x: abs(x), np.linalg.eigvalsh(A)))
    if d is None:
        d = round(evals[-1])

    cntr = 0
    for ev in reversed(evals):
        # Find all eigenvalues that are roughly d
        if ev > d - 0.001:
            cntr += 1
            continue
        if cntr == 0:
            logging.warn("Irregular graph given")
        if cntr == 2:
            logging.info("Bipartite graph given")
        if cntr > 2:
            logging.warning("Disconnected graph given")

        # Check if the next eigenvalue (first nontrivial one) is within the bounds
        return ev

def spectral_gap(A: np.array) -> float:
    evals = sorted(map(lambda x: abs(x), np.linalg.eigvalsh(A)))
    return evals[-1] - evals[-2]

if __name__=="__main__":
    nonramanujan = np.array(
    [
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
    ]
    )
    assert not is_ramanujan(nonramanujan)