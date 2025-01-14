from collections import defaultdict
from typing import Optional
from multiprocessing import Pool
from statistics import mean

from random_regular import random_regular
from utils import is_ramanujan, second_eigenvalue

from tqdm import tqdm

attempts_per_size = 10
vertex_step = 2
max_size = 100
d = 10
starting_vertices = d + 1
assert starting_vertices > d

processes = 4
total=attempts_per_size * (max_size - starting_vertices+1) // vertex_step

# output of form (n, proportion)

def proportion_mp(d: Optional[int] = None):
    # Wraps is_ramanujan to return number of vertices
    def prop(n: int) -> tuple[int, Optional[float]]:
        A = random_regular(n, d)
        if A is None:
            return (n, None)
        return (n, 1 if is_ramanujan(A, d) else 0)

    return prop

def iterate():
    vertices = starting_vertices
    while vertices < max_size:
        for _attempt in range(attempts_per_size):
            yield vertices

        vertices += vertex_step

def coalesce(results: dict[int, list[float]]):
    all_results = []
    for n, res in results.items():
        all_results.append((n, mean(res)))
    sorted(all_results, key=lambda x: x[0])
    for n, res in all_results:
        print(f"({n}, {mean(res)})")


def proportion_body_mp(n: int) -> tuple[int, Optional[float]]:
    A = random_regular(n, d)
    if A is None:
        return (n, None)
    return (n, 1 if is_ramanujan(A, d) else 0)

def proportion():
    with Pool(processes) as pool:
        results = defaultdict(list)
        for result in tqdm(pool.imap_unordered(proportion(d), iterate()),  total=total):
            if result[1] is not None:
                results[results[0]].append(result[1])

        coalesce(results)


def average_second_mp_body(n: int) -> tuple[int, Optional[float]]:
    A = random_regular(n, d)
    if A is None:
        return (n, None)
    return (n, second_eigenvalue(A, d))

def average_second():
    with Pool(processes) as pool:
        results = defaultdict(list)
        for result in tqdm(pool.imap_unordered(average_second_mp_body, iterate()), total=total):
            if result[1] is not None:
                results[result[0]].append(result[1])

        coalesce(results)

pass
average_second()
#proportion()