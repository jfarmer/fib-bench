# Binet's formula
require_relative "phi_rational"

# Binet's formula:
# F(N) = (phi^N - (1 - phi)^N)/(2*phi - 1)
def fib_phi(n)
  ((PhiRational(0,1)**n - PhiRational(1,-1)**n)/PhiRational(-1, 2)).a.to_i
end

if __FILE__ == $PROGRAM_NAME
  if ARGV.empty?
    puts "Missing required argument <N>"
    puts ""
    puts "Usage:"
    puts "  ruby #{$PROGRAM_NAME} <N>     # Calculate the Nth Fibonacci number"
    exit 1
  end

  n = ARGV[0].to_i

  puts fib_phi(n)
end
