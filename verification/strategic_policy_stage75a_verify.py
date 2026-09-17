import sympy as sp
import random, math

# Symbols
x1,x2,a,D,c,rho,B = sp.symbols('x1 x2 a D c rho B', positive=True, finite=True)
p,d = sp.symbols('p d', real=True)

# Payoffs
U1=(a+D)*x1-c*x1**2/2-rho*x1*x2 + a*(B-x1)-c*(B-x1)**2/2-rho*(B-x1)*(B-x2)
U2=(a+D)*x2-c*x2**2/2-rho*x1*x2 + a*(B-x2)-c*(B-x2)**2/2-rho*(B-x1)*(B-x2)

# 1. Government FOC/SOC
FOC1=sp.expand(sp.diff(U1,x1))
FOC1_expected=D+B*(c+rho)-2*c*x1-2*rho*x2
assert sp.simplify(FOC1-FOC1_expected)==0
assert sp.simplify(sp.diff(U1,x1,2)+2*c)==0

# 2. Interior symmetric Nash solution
xN=sp.solve(sp.Eq(FOC1_expected.subs(x2,x1),0),x1)[0]
xN_expected=B/2+D/(2*(c+rho))
assert sp.simplify(xN-xN_expected)==0
# Interior/corner boundary xN=B iff B=D/(c+rho)
assert sp.simplify((xN_expected-B) + (B*c+B*rho-D)/(2*(c+rho)))==0

# 3. Coordinator transformation
W=sp.expand(U1+U2)
Wpd=sp.expand(W.subs({x1:B/2+p+d,x2:B/2+p-d}))
C0=sp.simplify(Wpd.subs({p:0,d:0}))
Wrel=sp.expand(sp.simplify(Wpd-C0))
Wrel_expected=2*D*p-2*(c+2*rho)*p**2-2*(c-2*rho)*d**2
assert sp.simplify(Wrel-Wrel_expected)==0

# 4. For rho>c/2, maximize |d| at fixed p: |d| = B/2-|p|.
Wp_pos=sp.expand(Wrel_expected.subs(d,B/2-p))
Wp_neg=sp.expand(Wrel_expected.subs(d,B/2+p))
# Positive branch optimum
p_pos=sp.solve(sp.Eq(sp.diff(Wp_pos,p),0),p)[0]
p_pos_expected=(D+B*(c-2*rho))/(4*c)
assert sp.simplify(p_pos-p_pos_expected)==0
# Negative branch unconstrained optimum is positive under rho>c/2 and D>0, so negative branch max is p=0.
p_neg=sp.solve(sp.Eq(sp.diff(Wp_neg,p),0),p)[0]
assert sp.simplify(p_neg-(D+B*(2*rho-c))/(4*c))==0

# 5. Coordinator lower allocation when asymmetric
zP=sp.simplify(2*p_pos_expected)
zP_expected=(D+B*(c-2*rho))/(2*c)
assert sp.simplify(zP-zP_expected)==0
# Threshold identities
assert sp.simplify((zP_expected-B) + (B*c+2*B*rho-D)/(2*c))==0       # asymmetry iff D < B(c+2rho)
assert sp.simplify((zP_expected-B/2) + (2*B*rho-D)/(2*c))==0          # strict differentiation iff D < 2rho B
assert sp.simplify(zP_expected-(B*c-2*B*rho+D)/(2*c))==0             # full specialization iff D <= B(2rho-c)

# 6. Headline region implies interior Nash: D/(2rho) > D/(c+rho) when rho<c.
diff_threshold=sp.factor(D/(2*rho)-D/(c+rho))
assert sp.simplify(diff_threshold-D*(c-rho)/(2*rho*(c+rho)))==0

# 7. Randomized global property checks in production domain.
def br(xj,D,c,rho,B):
    raw=(D+B*(c+rho)-2*rho*xj)/(2*c)
    return max(0.0,min(B,raw))

def coord_value(x1,x2,D,c,rho,B):
    # omit constants a terms because they do not affect maximization
    return (D*x1 - c*x1*x1/2 - rho*x1*x2
            -c*(B-x1)**2/2 - rho*(B-x1)*(B-x2)
            +D*x2 - c*x2*x2/2 - rho*x1*x2
            -c*(B-x2)**2/2 - rho*(B-x1)*(B-x2))

rng=random.Random(20260917)
for _ in range(10000):
    c0=10**rng.uniform(-1,1)
    rho0=rng.random()*0.999*c0
    D0=10**rng.uniform(-2,1)
    B0=10**rng.uniform(-2,2)
    # closed-form unique NE
    xN0=min(B0, B0/2 + D0/(2*(c0+rho0)))
    assert abs(br(xN0,D0,c0,rho0,B0)-xN0) < 1e-9
    assert xN0 > B0/2 - 1e-12
    # headline iff differentiation, away from exact boundary
    if rho0 > c0/2:
        z=max(0.0,(D0+B0*(c0-2*rho0))/(2*c0))
        differentiated = z < B0/2 - 1e-12
        condition = B0 > D0/(2*rho0) + 1e-12
        if abs(B0-D0/(2*rho0)) > 1e-8:
            assert differentiated == condition

# 8. Random global coordinator dominance checks against 100 random feasible allocations per draw.
def Wred(x1,x2,D,c,rho,B):
    return (D*(x1+x2)
            - c/2*(x1*x1+x2*x2+(B-x1)**2+(B-x2)**2)
            - 2*rho*(x1*x2+(B-x1)*(B-x2)))

def coord_candidates(D,c,rho,B):
    if rho < c/2:
        x=min(B, B/2 + D/(2*(c+2*rho)))
        return [(x,x)]
    if abs(rho-c/2) < 1e-12:
        if B <= D/(2*c):
            return [(B,B)]
        # continuum; return symmetric representative with optimal mean
        s=B + D/(2*c)
        return [(s/2,s/2)]
    # rho > c/2
    if B <= D/(c+2*rho):
        return [(B,B)]
    z=max(0.0,(D+B*(c-2*rho))/(2*c))
    return [(B,z),(z,B)]

rng2=random.Random(20260918)
for _ in range(2000):
    c0=10**rng2.uniform(-1,1)
    rho0=rng2.random()*0.999*c0
    D0=10**rng2.uniform(-2,1)
    B0=10**rng2.uniform(-2,2)
    cand=coord_candidates(D0,c0,rho0,B0)
    wc=max(Wred(xx,yy,D0,c0,rho0,B0) for xx,yy in cand)
    for __ in range(100):
        xx=rng2.random()*B0
        yy=rng2.random()*B0
        assert wc + 1e-9 >= Wred(xx,yy,D0,c0,rho0,B0)

# 9. Exact boundary-value identities.
B1=D/(c+2*rho)
assert sp.simplify(zP_expected.subs(B,B1)-B1)==0
B2=D/(2*rho)
assert sp.simplify(zP_expected.subs(B,B2)-B2/2)==0
B3=D/(2*rho-c)
assert sp.simplify(zP_expected.subs(B,B3))==0

print('STAGE 7.5A FORMAL VERIFICATION: PASS')
print('Verified symbolic identities: FOC, SOC, Nash formula, W(p,d), coordinator branches, threshold equivalences.')
print('Randomized checks: 10,000 theorem-condition draws + 2,000 global coordinator draws x 100 feasible deviations; no counterexamples.')
