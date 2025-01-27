from math import sqrt


def get_reprs(p,q):
    num_representations = p+1
    all_representations = []

    for i in range(1, int(sqrt(p+1)+1), 2):
        for j in range(-int(sqrt(p+1)+1), int(sqrt(p+1)+1)):
            if j % 2 != 0:
                continue
            for k in range(-int(sqrt(p+1)+1), int(sqrt(p+1)+1)):
                if k % 2 != 0:
                    continue
                for l in range(-int(sqrt(p+1)+1), int(sqrt(p+1)+1)):
                    if l % 2 != 0:
                        continue
                    if i**2 + j**2 + k**2 + l**2 == p:
                        all_representations.append([i, j, k, l])
    
    assert len(all_representations) == num_representations
    return all_representations

def legendre(p,q):
    if p % q == 0:
        return 0
    for n in range(q):
        if (n*n) % q == p:
            return 1

    return -1 

def legendre_print(p,q):
    if p % q == 0:
        return 0
    for n in range(q):
        if (n*n) % q == p:
            print(f"{n}*{n}={p}  (mod {q})")
            return 1

    return -1 

# our p < q
primes = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271]

reduced_primes = []
for prime in primes:
    if prime % 4 == 1:
        reduced_primes.append(prime)

# Find pairs of primes with p < q and (p/q) == 1

def matching_pair(p,q):
    if legendre(p,q) == 1:
        return True
    return False

filtered_pairs = []

for q_idx in range(len(reduced_primes)):
    q = reduced_primes[q_idx]
    for p_idx in range(q_idx):
        p = reduced_primes[p_idx]
        if matching_pair(p,q):
            filtered_pairs.append((p,q))

print(filtered_pairs)
legendre_print(13, 17)
p, q = filtered_pairs[3]
print(f"p={p}    q={q}")
legendre_print(p,q)

# WE CAN DIVIDE THE MATRIX BY [n^-1 0; 0 n^-1]
# This way the determinant -> 1
"""
Če je p=n² mod q potem je n liho število 
in da se napisati (n, 0, 0, 0) za izbiro alpha
-> njen inverz

ojoj potrebno je še preveriti če so inverzi kandidatov tudi kandidati...

primer: p=13, q=17
13 = 8^2 + 0 + 0 + 0   (mod 17)
[ 8  0 ]
[ 0  8 ] je element grupe
determinanta = 13 != 1

8^-1 = 15
[15 0]
[0 15] je inverz zgornjega elementa
determinanta = 4 != 13
"""
