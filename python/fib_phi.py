from phi_rational import *

def fib_phi(n):
    return int((PhiRational(0,1)**n - PhiRational(1,-1)**n) / PhiRational(-1, 2))
