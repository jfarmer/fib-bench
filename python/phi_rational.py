from fractions import Fraction

class PhiRational:
    PHI = 1.61803398875

    def __init__(self, a, b = 0):
        if isinstance(a, PhiRational):
            self.a = a.a
            self.b = a.b
        else:
            self.a = Fraction(a)
            self.b = Fraction(b)

    def inverse(self):
        return PhiRational(-self.a, -self.b)

    def norm(self):
        return Fraction(self.a**2 + self.a*self.b - self.b**2)

    def reciprocal(self):
        return PhiRational((self.a + self.b) / self.norm(), -self.b / self.norm())

    def __int__(self):
        if self.b == 0:
            return int(self.a)
        else:
            return int(self.a + self.b * PhiRational.PHI)

    def __add__(self, other):
        other = PhiRational(other)

        return PhiRational(self.a + other.a, self.b + other.b)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + other.inverse()

    def __mul__(self, other):
        other = PhiRational(other)

        a, b = self.a, self.b
        c, d = other.a, other.b

        return PhiRational(a*c + b*d, a*d + b*c + b*d)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * PhiRational(other).reciprocal()

    def __eq__(self, other):
        other = PhiRational(other)
        return self.a == other.a and self.b == other.b

    def __pow__(self, n):
        base   = PhiRational(self.a, self.b)
        result = PhiRational(1, 0)

        while n != 0:
            if n % 2 == 1:
                result *= base
                n -= 1

            base *= base
            n //= 2

        return result

    def __repr__(self):
        return f'({self.a} + {self.b}φ)'
