import sympy as sp

# Stage 11 hostile-referee stress test:
# allow sector-specific overlap costs rho_A and rho_B while keeping
# the frozen benchmark otherwise unchanged.

x1, x2, a, D, c, B, rA, rB = sp.symbols(
    'x1 x2 a D c B rA rB', positive=True, finite=True
)
p, d = sp.symbols('p d', real=True)

U1 = ((a + D) * x1 - c * x1**2 / 2 - rA * x1 * x2
      + a * (B - x1) - c * (B - x1)**2 / 2
      - rB * (B - x1) * (B - x2))
U2 = ((a + D) * x2 - c * x2**2 / 2 - rA * x1 * x2
      + a * (B - x2) - c * (B - x2)**2 / 2
      - rB * (B - x1) * (B - x2))

# Decentralized FOC and symmetric interior equilibrium.
foc = sp.expand(sp.diff(U1, x1))
foc_expected = D + B * (c + rB) - 2 * c * x1 - (rA + rB) * x2
assert sp.simplify(foc - foc_expected) == 0

xN = sp.solve(sp.Eq(foc_expected.subs(x2, x1), 0), x1)[0]
xN_expected = (D + B * (c + rB)) / (2 * c + rA + rB)
assert sp.simplify(xN - xN_expected) == 0

orientation_gap = sp.factor(xN - B / 2)
orientation_expected = (2 * D + B * (rB - rA)) / (2 * (2 * c + rA + rB))
assert sp.simplify(orientation_gap - orientation_expected) == 0

# Joint best-response contraction slope in sup norm.
br_slope = sp.simplify((rA + rB) / (2 * c))

# Coordinator transformation.
W = sp.expand(U1 + U2)
Wpd = sp.expand(W.subs({x1: B / 2 + p + d, x2: B / 2 + p - d}))
W0 = sp.expand(Wpd.subs({p: 0, d: 0}))
Wrel = sp.factor(sp.expand(Wpd - W0))
Wrel_expected = (
    2 * (D - B * (rA - rB)) * p
    - 2 * (c + rA + rB) * p**2
    - 2 * (c - rA - rB) * d**2
)
assert sp.simplify(Wrel - Wrel_expected) == 0

# On the A-high edge (x1=B, x2=z), the low-A allocation is:
z = sp.symbols('z', real=True)
Wedge = sp.expand(W.subs({x1: B, x2: z}))
zstar = sp.solve(sp.Eq(sp.diff(Wedge, z), 0), z)[0]
zstar_expected = (D + B * (c - 2 * rA)) / (2 * c)
assert sp.simplify(zstar - zstar_expected) == 0
assert sp.simplify(zstar - B / 2 - (D - 2 * B * rA) / (2 * c)) == 0

# Recovery of the frozen benchmark rA=rB=rho.
rho = sp.symbols('rho', positive=True, finite=True)
assert sp.simplify(orientation_gap.subs({rA: rho, rB: rho}) - D / (2 * (c + rho))) == 0
assert sp.simplify(Wrel_expected.subs({rA: rho, rB: rho})
                   - (2 * D * p - 2 * (c + 2 * rho) * p**2
                      - 2 * (c - 2 * rho) * d**2)) == 0
assert sp.simplify(zstar_expected.subs(rA, rho)
                   - (D + B * (c - 2 * rho)) / (2 * c)) == 0

print('STAGE 11 SECTOR-SPECIFIC OVERLAP STRESS: PASS')
print('Symmetric interior NE:', xN_expected)
print('NE orientation gap:', orientation_expected)
print('BR contraction slope:', br_slope)
print('Coordinator relative welfare:', Wrel_expected)
print('A-high-edge low allocation:', zstar_expected)
print('Implication: equal-rho is not a knife-edge for fixed parameters,')
print('but sufficiently large B can reverse decentralized orientation when rho_A > rho_B.')
