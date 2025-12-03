#!/usr/bin/env python3
import pyperf

from fib_iterative import fib_iterative
from fib_phi import fib_phi
from fib_matrix import fib_matrix

runner = pyperf.Runner()
runner.argparser.add_argument('N', nargs='?', type=int, default=30000,
                              help='Fibonacci number to compute')
args = runner.parse_args()
N = args.N

runner.bench_func('fib_iterative', fib_iterative, N)
runner.bench_func('fib_phi', fib_phi, N)
runner.bench_func('fib_matrix', fib_matrix, N)
