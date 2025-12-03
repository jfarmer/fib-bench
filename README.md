# fib-bench

Benchmark of a few Ruby and Python implementations of Fibonacci

The most interesting one is `fib_phi` which implements the exact arithmetic of ℚ(φ). This allows us to use Binet's formula without loss of accuracy.

## Contents <!-- omit in toc -->

- [Usage](#usage)
- [Binet's Formula](#binets-formula)
- [Isn't This Overkill?](#isnt-this-overkill)

## Usage

Clone this repository and run:

```console
ruby ruby/fib_bench.rb
```

There are also Python implementations in the `python/` directory, but it requires `numpy` for the matrix implementation. You will want to:

```console
cd python/
uv run python fib_bench.py
```

## Binet's Formula

Binet's formula is closed-form expression for the n<sup>th</sup> Fibonacci number. The formula is:

```text
(φ**n - (1 - φ)**n) / sqrt(5)
```

where `φ` is the Golden ratio

```text
φ^2 - φ + 1 = 0
φ = (1 + sqrt(5)) / 2
```

The naive implementation of Binet's formula where we approximate `φ` with a `double` doesn't work. For large `n`, floating point errors cause incorrect results.

BUT! We **_can_** use Binet's formula if we implement exact arithmetic on ℚ(φ).

ℚ is the set of all rational numbers and ℚ(φ) is the set of all numbers of the form

```text
a + bφ
```

where `a` and `b` are rational numbers. The sum and product of any two numbers ℚ(φ) are also in ℚ(φ), so in the same way that `Rational(1,2)` exactly represents `1/2`, we can create a `PhiRation(a, b)` that represents `a + bφ`.

Binet's formula then becomes

```ruby
((PhiRational(0,1)**n - PhiRational(1,-1)**n)/PhiRational(-1, 2))
```

## Isn't This Overkill?

Yes. This is meant to be pedagogical.
