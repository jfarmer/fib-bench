# Helper method for creating phi-rational numbers.
def PhiRational(a, b = 0)
  case a
  when PhiRational
    a
  else
    PhiRational.new(a, b)
  end
end

class PhiRational
  attr_reader :a, :b

  def initialize(a, b)
    @a = Rational(a)
    @b = Rational(b)
  end

  # (a + b*p) + (c + d*p) = (a + c) + (b + d)*p
  def +(other)
    other = PhiRational(other)

    PhiRational(a + other.a, b + other.b)
  end

  def -(other)
    self + PhiRational(other).inverse
  end

  # -(a + b*p) = -a + -b*p
  def inverse
    PhiRational(-a, -b)
  end

  # |a + b*p| = a^2 + a*b - b^2
  def norm
    Rational(a*a + a*b - b*b)
  end

  # (a + b*p) * (c + d*p) = (a*c + b*d) + (a*d + b*c + b*d)*p
  def *(other)
    other = PhiRational(other)

    c = other.a
    d = other.b

    PhiRational(a*c + b*d, a*d + b*c + b*d)
  end

  def /(other)
    self * PhiRational(other).reciprocal
  end

  # 1/(a + b*p) == (a + b)/(a^2 - a*b + b^2) - (b*p)/(a^2 - a*b + b^2)
  def reciprocal
    PhiRational((a + b)/self.norm, -b/self.norm)
  end

  def ==(other)
    a == PhiRational(other).a && b == PhiRational(other).b
  end

  def **(n)
    base   = PhiRational(a, b)
    result = PhiRational(1, 0)

    while n.nonzero?
      if n.odd?
        result *= base
        n -= 1
      end

      base *= base
      n /= 2
    end

    result
  end

  def to_s
    "(#{a}) + (#{b})p"
  end
  alias_method :inspect, :to_s
end
