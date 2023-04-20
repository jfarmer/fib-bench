import functools
import sys

sys.setrecursionlimit(70000)
sys.set_int_max_str_digits(100000)

# @functools.cache
def fib_recursive(n):
    if n == 0: return 0
    if n == 1: return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)
