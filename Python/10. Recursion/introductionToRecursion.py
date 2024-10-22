def factorial(n): # n * (n-1) * (n-2) * ... * 3 * 2 * 1
  if n == 0 or n == 1:
      return 1
  else:
      return n * factorial(n - 1)


print(factorial(5))

# 5!
# = 5 * 4!
# = 5 * 4 * 3!
# = 5 * 4 * 3 * 2!
# = 5 * 4 * 3 * 2 * 1

# factorial(5)
# |
# +-- factorial(4)
#     |
#     +-- factorial(3)
#         |
#         +-- factorial(2)
#             |
#             +-- factorial(1)
