from random_regular import random_regular
from utils import is_ramanujan, second_eigenvalue


attempts_per_size = 10
vertex_step = 2
max_size = 100
d = 10


# output of form (n, proportion)

def proportion():
    vertices = d + 1
    while vertices < max_size:
        n_ramanujan = 0
        curr_attempts = 0
        for _ in range(attempts_per_size):
            A = random_regular(vertices, d)
            if A is None:
                continue

            curr_attempts += 1
            if is_ramanujan(A, d):
                n_ramanujan += 1
        print(f"({vertices}, {n_ramanujan/curr_attempts})")
        vertices += vertex_step


def average_second():
    vertices = d + 1
    while vertices < max_size:
        curr_attempts = 0
        eival_sum = 0
        for _ in range(attempts_per_size):
            A = random_regular(vertices, d)
            if A is None:
                # did not find the graph in max_attempts
                continue

            curr_attempts += 1
            eival_sum += second_eigenvalue(A, d)
        
        if curr_attempts != 0:
            print(f"({vertices}, {eival_sum/curr_attempts})")
        vertices += vertex_step

pass
average_second()
#proportion()