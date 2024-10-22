# Fibonacci Sequence
# 0, 1, 1, 2, 3, 5, 8, ...

# F(n) = F(n-1) + F(n-2)
# F(0) = 0, F(1) = 1

# Example:
# F(5) = F(4) + F(3)
#      = F(3) + F(2) + F(2) + 1
#      = F(2) + 1 + 1 + 1 + 1
#      = 1 + 4
#      = 5

def fibonacci(n, memo={}):
  if n in memo:
    return memo[n]
  
  # base case
  if n <= 1:
    return n

  # recursive case
  memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
  return memo[n]

print(fibonacci(5))