# Implementation of Binet's formula
require_relative "fib_phi"

# Basic iterative version
def fib_iterative(n)
  return 0 if n == 0
  return 1 if n == 1

  a, b = 0, 1

  2.upto(n) do |i|
    a, b = b, a + b
  end

  b
end

# In time: O(n)
# In memory: O(n)
def fib_recursive(n, cache = {})
  return 0 if n == 0
  return 1 if n == 1
  return cache[n] if cache.key?(n)

  cache[n] = fib_recursive(n - 1, cache) + fib_recursive(n - 2, cache)

  cache[n]
end

# Matrix solution
require "matrix"

FIB_MATRIX = Matrix[[1,1],[1,0]]
def fib_matrix(n)
  (FIB_MATRIX**(n-1))[0,0]
end

require "benchmark"

# Note: if the input is too large, the recursive solution will
#       recurse too much and crash

N = ARGV.fetch(0) { 30000 }.to_i

ITERATIONS = 50

puts ""
puts "Benchmarking fib(#{N})..."
puts ""

Benchmark.bmbm do |x|
  x.report("fib_iterative") do
    ITERATIONS.times { fib_iterative(N) }
  end

  x.report("fib_phi") do
    ITERATIONS.times { fib_phi(N) }
  end

  x.report("fib_matrix") do
    ITERATIONS.times { fib_matrix(N) }
  end
end
