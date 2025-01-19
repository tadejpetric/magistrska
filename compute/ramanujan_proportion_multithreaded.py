from collections import defaultdict
from typing import Optional
from multiprocessing import Pool
from statistics import mean

from random_regular_networkx import random_regular
from utils import is_ramanujan, second_eigenvalue

from tqdm import tqdm

attempts_per_size = 200
vertex_step = 50
max_size = 3001
d = 10
starting_vertices = 100
assert starting_vertices > d

processes = 10
total = ((max_size - starting_vertices + vertex_step - 1) // vertex_step) * attempts_per_size


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
        print(f"({n}, {res})")


def proportion_body_mp(n: int) -> tuple[int, Optional[float]]:
    A = random_regular(n, d)
    if A is None:
        return (n, None)
    return (n, 1 if is_ramanujan(A, d) else 0)

def proportion():
    with Pool(processes) as pool:
        results = defaultdict(list)
        for result in tqdm(pool.imap_unordered(proportion_body_mp, iterate()),  total=total):
            if result[1] is not None:
                results[result[0]].append(result[1])

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

print("Second eigenvalue")
average_second()
print("Proportion")
proportion()