# Implementation of matrix groups over Zq


class Zqint:
    def __init__(self, val, q):
        if isinstance(val, Zqint):
            self.val = val.val % q
            assert val.q == q
            self.q = q
        else:
            self.val = val % q
            self.q = q

    def __add__(self, other):
        return Zqint((self.val + other.val) % self.q, self.q)

    def __sub__(self, other):
        return Zqint((self.val - other.val) % self.q, self.q)

    def __mul__(self, other):
        return Zqint((self.val * other.val) % self.q, self.q)

    def __eq__(self, other):
        return self.val % self.q == other.val % self.q
    
    def __str__(self):
        return str(self.val)

    def minv(self):
        for i in range(self.q):
            if (self.val * i) % self.q == 1:
                return Zqint(i, self.q)
        return None

    def ainv(self):
        return Zqint((-self.val) % self.q, self.q)

    @staticmethod
    def get_i(q):
        for i in range(q):
            if (i * i) % q == q - 1:
                return i


class Matrix:
    def __init__(self, a, b, c, d, q):
        self.a = Zqint(a, q)
        self.b = Zqint(b, q)
        self.c = Zqint(c, q)
        self.d = Zqint(d, q)
        self.q = q

    def __add__(self, other: "Matrix"):
        assert self.q == other.q
        return Matrix(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d,
            self.q,
        )

    def __sub__(self, other: "Matrix"):
        assert self.q == other.q
        return Matrix(
            self.a - other.a,
            self.b - other.b,
            self.c - other.c,
            self.d - other.d,
            self.q,
        )

    def __mul__(self, other):
        if isinstance(other, Zqint):
            return Matrix(
                (self.a * other).val,
                (self.b * other).val,
                (self.c * other).val,
                (self.d * other).val,
                self.q,
            )
        assert self.q == other.q
        return Matrix(
            self.a * other.a + self.b * other.c,
            self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c,
            self.c * other.b + self.d * other.d,
            self.q,
        )

    def determinant(self):
        return self.a * self.d - self.b * self.c

    def __str__(self):
        return (
            f"[{self.a.val: 3d} {self.b.val: 3d}\n {self.c.val: 3d} {self.d.val: 3d}]"
        )

    def __eq__(self, other):
        return (
            self.a == other.a
            and self.b == other.b
            and self.c == other.c
            and self.d == other.d
        )

    def minv(self):
        det = self.determinant()
        if det == Zqint(0, self.q):
            return None
        matrix = Matrix(self.d, self.b.ainv().val, self.c.ainv().val, self.a, self.q)
        return matrix * det.minv()


from SL_generators import get_reprs, legendre

p = 13
q = 53

imag = Zqint.get_i(q)

test_num = Zqint(p, q)
print(test_num.minv())

def print_repr(repr):
    a, b, c, d = repr
    print(f"{a}, {b}, {c}, {d}")
    matrix = Matrix(
        a + imag * b,
        c + imag * d,
        -c + imag * d,
        a - imag * b,
        q,
    )
    print(matrix)
    print(f"det(A) = {matrix.determinant().val}")
    print("--------------")


reprs = get_reprs(p, q)
for repr in reprs:
    print_repr(repr)
