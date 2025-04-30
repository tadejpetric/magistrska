from math import isqrt
from itertools import product

import numpy as np
# ------------------------------------------------------------
# 1)  Four–square representations a^2+b^2+c^2+d^2 = p
# ------------------------------------------------------------
def four_square_reprs(p: int) -> list[tuple[int, int, int, int]]:
    """
    Enumerate the (p+1) representations required by the LPS
    construction:
        • a is odd
        • b, c, d are even
        • a^2 + b^2 + c^2 + d^2  =  p
    The brute-force range ±⌊√(p)⌋ already suffices, but using
    the parity hints keeps the loop small.
    """
    bound = isqrt(p+1) + 1
    reps  = []

    for a in range(1, bound, 2):                 # odd
        for b, c, d in product(range(-bound, bound + 1), repeat=3):  # even
            if a*a + b*b + c*c + d*d == p:
                reps.append((a, b, c, d))

    # The LPS theorem guarantees exactly p+1 such reps.
    assert len(reps) == p + 1, "Did not find p+1 representations"
    return reps


# ------------------------------------------------------------
# 2)  A square‑root of −1  mod q  (q ≡ 1 (mod 4) prime)
# ------------------------------------------------------------
def mod_i(q: int) -> int:
    """Return the least  i ∈ [0,q)  with  i² ≡ −1 mod q."""
    for i in range(q):
        if (i * i) % q == q - 1:
            return i
    raise ValueError(f"{q} has no square‑root of −1 (q must be prime ≡ 1 mod 4)")


# ------------------------------------------------------------
# 3)  Lift one representation to a 2×2 generator matrix
# ------------------------------------------------------------
def lift(rep: tuple[int, int, int, int], q: int, imag: int) -> list[list[int]]:
    """
    Map  (a,b,c,d)  ↦  [[a+ib,  c+id], [‑c+id,  a‑ib]]  in  SL₂(𝔽_q).
    All arithmetic is performed mod q.
    """
    a, b, c, d = rep
    return [
        [(a + imag * b) % q,  (c + imag * d) % q],
        [(-c + imag * d) % q, (a - imag * b) % q],
    ]


# ------------------------------------------------------------
# 4)  Convenience wrapper – the full LPS generator set
# ------------------------------------------------------------
def lps_generators(p: int, q: int) -> list[list[list[int]]]:
    """
    Return the  p+1  LPS generators for  X^{p,q}.
       • p, q  primes with  p ≡ 1 (mod 4),  q ≡ 1 (mod 4),
         and  (p/q) = 1  (q is a quadratic residue mod p).
    No attempt at efficiency is made - the goal is clarity.
    """
    reps  = four_square_reprs(p)
    imag  = mod_i(q)
    return [np.array(lift(rep, q, imag)) for rep in reps]


# ------------------------------------------------------------
# 5)  Demo
# ------------------------------------------------------------
if __name__ == "__main__":
    p, q = 5, 29          # the first non‑trivial LPS pair
    gens = lps_generators(p, q)

    print(f"{len(gens)} generators found (should be {p+1}).\n")
    for idx, g in enumerate(gens, 1):
        print(f"g{idx} =\n{g}")
