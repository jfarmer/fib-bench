import pytest
from fractions import Fraction
from phi_rational import PhiRational


class TestConstruction:
    def test_from_integers(self):
        p = PhiRational(3, 2)
        assert p.a == Fraction(3)
        assert p.b == Fraction(2)

    def test_from_single_integer(self):
        p = PhiRational(5)
        assert p.a == Fraction(5)
        assert p.b == Fraction(0)

    def test_from_phi_rational(self):
        p1 = PhiRational(3, 2)
        p2 = PhiRational(p1)
        assert p2.a == Fraction(3)
        assert p2.b == Fraction(2)

    def test_from_fractions(self):
        p = PhiRational(Fraction(1, 2), Fraction(3, 4))
        assert p.a == Fraction(1, 2)
        assert p.b == Fraction(3, 4)


class TestArithmetic:
    def test_add_two_phi_rationals(self):
        p1 = PhiRational(1, 2)
        p2 = PhiRational(3, 4)
        result = p1 + p2
        assert result == PhiRational(4, 6)

    def test_add_phi_rational_and_int(self):
        p = PhiRational(1, 2)
        result = p + 5
        assert result == PhiRational(6, 2)

    def test_radd_int_and_phi_rational(self):
        p = PhiRational(1, 2)
        result = 5 + p
        assert result == PhiRational(6, 2)

    def test_sub_two_phi_rationals(self):
        p1 = PhiRational(5, 3)
        p2 = PhiRational(2, 1)
        result = p1 - p2
        assert result == PhiRational(3, 2)

    def test_sub_phi_rational_and_int(self):
        p = PhiRational(5, 2)
        result = p - 3
        assert result == PhiRational(2, 2)

    def test_mul_two_phi_rationals(self):
        # (1 + 1φ) * (1 + 1φ) = 1 + φ + φ + φ² = 1 + 2φ + (φ+1) = 2 + 3φ
        p = PhiRational(1, 1)
        result = p * p
        assert result == PhiRational(2, 3)

    def test_mul_phi_rational_and_int(self):
        p = PhiRational(2, 3)
        result = p * 2
        assert result == PhiRational(4, 6)

    def test_rmul_int_and_phi_rational(self):
        p = PhiRational(2, 3)
        result = 2 * p
        assert result == PhiRational(4, 6)

    def test_div_two_phi_rationals(self):
        p1 = PhiRational(2, 3)
        p2 = PhiRational(1, 1)
        result = p1 / p2
        # Verify by multiplying back
        assert result * p2 == p1


class TestPower:
    def test_power_of_zero(self):
        p = PhiRational(3, 2)
        result = p ** 0
        assert result == PhiRational(1, 0)

    def test_power_of_one(self):
        p = PhiRational(3, 2)
        result = p ** 1
        assert result == PhiRational(3, 2)

    def test_power_of_two(self):
        # (1 + 1φ)² = 2 + 3φ (golden ratio property: φ² = φ + 1)
        p = PhiRational(1, 1)
        result = p ** 2
        assert result == PhiRational(2, 3)

    def test_power_of_phi(self):
        # φ^n follows Fibonacci: φ^n = F(n-1) + F(n)φ
        phi = PhiRational(0, 1)
        assert phi ** 1 == PhiRational(0, 1)  # F(0) + F(1)φ = 0 + 1φ
        assert phi ** 2 == PhiRational(1, 1)  # F(1) + F(2)φ = 1 + 1φ
        assert phi ** 3 == PhiRational(1, 2)  # F(2) + F(3)φ = 1 + 2φ
        assert phi ** 4 == PhiRational(2, 3)  # F(3) + F(4)φ = 2 + 3φ
        assert phi ** 5 == PhiRational(3, 5)  # F(4) + F(5)φ = 3 + 5φ

    def test_power_of_phi_101(self):
        # φ^101 = F(100) + F(101)φ
        phi = PhiRational(0, 1)
        result = phi ** 101
        assert result == PhiRational(354224848179261915075, 573147844013817084101)


class TestNormAndReciprocal:
    def test_norm_of_phi(self):
        # Norm of φ = 0² + 0*1 - 1² = -1
        phi = PhiRational(0, 1)
        assert phi.norm() == Fraction(-1)

    def test_norm_of_one_plus_phi(self):
        # Norm of (1 + φ) = 1 + 1 - 1 = 1
        p = PhiRational(1, 1)
        assert p.norm() == Fraction(1)

    def test_reciprocal_times_original_is_one(self):
        p = PhiRational(2, 3)
        result = p * p.reciprocal()
        assert result == PhiRational(1, 0)


class TestEquality:
    def test_equal_phi_rationals(self):
        p1 = PhiRational(3, 2)
        p2 = PhiRational(3, 2)
        assert p1 == p2

    def test_unequal_phi_rationals(self):
        p1 = PhiRational(3, 2)
        p2 = PhiRational(2, 3)
        assert not (p1 == p2)

    def test_equal_to_int(self):
        p = PhiRational(5, 0)
        assert p == 5


class TestRepr:
    def test_repr(self):
        p = PhiRational(3, 2)
        assert repr(p) == '(3 + 2φ)'


class TestFibonacci:
    """Test that PhiRational correctly computes Fibonacci numbers via Binet's formula."""

    def test_fib_10(self):
        from fib_phi import fib_phi
        assert fib_phi(10) == 55

    def test_fib_20(self):
        from fib_phi import fib_phi
        assert fib_phi(20) == 6765

    def test_fib_50(self):
        from fib_phi import fib_phi
        assert fib_phi(50) == 12586269025
