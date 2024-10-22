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

def fibonacci_memoization(n, memo={}):
  if n in memo:
    return memo[n]

  # base case
  if n <= 1:
    return n

  # recursive case
  memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
  return memo[n]

def fibonacci_tabulation(n):
  if n <= 1:
    return n

  table = [0] * (n+1)
  table[1] = 1

  for i in range(2, n+1):
    table[i] = table[i-1] + table[i-2]

  return table[n]

print(fibonacci_tabulation(6))