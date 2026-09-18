"""Stage-1 regression checks for the N-region x M-sector baseline.

This file is verification support, not a proof and not a novelty certificate.
"""

from fractions import Fraction
from itertools import product

def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for k in range(total + 1):
        for tail in compositions(total - k, parts - 1):
            yield (k,) + tail

def planner_welfare(matrix, a, c, rho):
    n = len(matrix)
    m = len(matrix[0])
    X = [sum(matrix[i][s] for i in range(n)) for s in range(m)]
    sq = sum(matrix[i][s] ** 2 for i in range(n) for s in range(m))
    return sum(a[s] * X[s] - rho * X[s] ** 2 for s in range(m)) + (rho - c / 2) * sq

def diversified_rows(matrix):
    return sum(sum(v > 0 for v in row) >= 2 for row in matrix)

def grid_global_check(n, m, denominator, a, c, rho):
    rows = list(compositions(denominator, m))
    best = None
    maximizers = []
    for profile in product(rows, repeat=n):
        x = [[Fraction(v, denominator) for v in row] for row in profile]
        val = planner_welfare(x, a, c, rho)
        if best is None or val > best:
            best = val
            maximizers = [x]
        elif val == best:
            maximizers.append(x)
    return best, maximizers

def main():
    # 2x2 parent interior recovery.
    c = Fraction(5, 4)
    rho = Fraction(1, 2)
    B = Fraction(2, 1)
    Delta = Fraction(3, 4)
    qA = B / 2 + Delta / (2 * (c + rho))
    qB = B - qA
    assert qA + qB == B
    assert qA - qB == Delta / (c + rho)

    # Strong-overlap small-grid diagnostics: every grid-global maximizer
    # satisfies the analytic k <= M-1 support bound.
    cases = [
        (3, 2, 4, [Fraction(6,5), Fraction(1,1)]),
        (4, 3, 4, [Fraction(6,5), Fraction(1,1), Fraction(9,10)]),
    ]
    c = Fraction(1,1)
    rho = Fraction(3,4)  # c/2 < rho < c

    for n, m, den, a in cases:
        _, maximizers = grid_global_check(n, m, den, a, c, rho)
        assert maximizers
        assert all(diversified_rows(x) <= m - 1 for x in maximizers)

    # Equal-sector divisible benchmark: constructed balanced specialization
    # attains both analytic bounds.
    n, m = 6, 3
    B = Fraction(1,1)
    a0 = Fraction(1,1)
    matrix = []
    for s in range(m):
        for _ in range(n // m):
            row = [Fraction(0,1)] * m
            row[s] = B
            matrix.append(row)
    X = [sum(row[s] for row in matrix) for s in range(m)]
    assert X == [Fraction(n, m) * B] * m
    assert diversified_rows(matrix) == 0
    assert sum(v*v for row in matrix for v in row) == n * B * B

    print("Stage-1 N x M regression checks: PASS")

if __name__ == "__main__":
    main()
