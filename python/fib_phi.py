from phi_rational import *

# NOTE: Since ψ = -1/φ, we have ψ^n = (-1)^n / φ^n. This means we could
# compute φ^n once and derive ψ^n via reciprocal, cutting exponentiations
# in half. This makes it almost as fast as fib_matrix with numpy!

def fib_phi(n):
    φ = PhiRational(0, 1)
    ψ = PhiRational(1, -1)
    sqrt5 = PhiRational(-1, 2)

    return int((φ**n - ψ**n) / sqrt5)
