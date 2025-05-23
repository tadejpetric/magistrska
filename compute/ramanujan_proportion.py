from random_regular_naive import random_regular, is_random_ramanujan
from utils import second_eigenvalue
from tqdm import tqdm

attempts_per_size = 10000
vertex_step = 10_000
max_size = 24+1
d = 4
starting_vertices =  24#d + 1 
assert starting_vertices > d

processes = 10
total=attempts_per_size * (max_size - starting_vertices+1) // vertex_step

# output of form (n, proportion)

def proportion():
    vertices = starting_vertices
    while vertices < max_size:
        n_ramanujan = 0
        curr_attempts = 0
        for _ in tqdm(range(attempts_per_size)):
            n_ramanujan += is_random_ramanujan(vertices, d)
            curr_attempts += 1

        print(f"({vertices}, {n_ramanujan/curr_attempts})")
        vertices += vertex_step

def average_second():
    vertices = starting_vertices
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

#average_second()
proportion()
