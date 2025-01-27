from math import sqrt


primes = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271]
reduced_primes = []
for prime in primes:
    if prime % 4 == 1:
        reduced_primes.append(prime)

def print_reprs(p,q):
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

    print(len(all_representations))
    assert len(all_representations) == num_representations

    def get_div(num):
        if num < 0:
            x = q + num
        else:
            x = num
        return x % q

    reduced_representations = set()
    for representation in all_representations:
        a = get_div(representation[0])
        b = get_div(representation[1])
        c = get_div(representation[2])
        d = get_div(representation[3])
        reduced_representations.add((a, b, c, d))

    print(len(reduced_representations))

for p in reduced_primes:
    print("for p = ", p)
    print_reprs(p, 5)

print("p=101, q=29")
print(101%4, 29%4)
print_reprs(101, 29)