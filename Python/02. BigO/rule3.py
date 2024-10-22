def print_arrays(arr, arr2):  # O(n+m)
  for element in arr:
    print(element)

  for element in arr2:
    print(element)


arr = list(range(100))
arr2 = list(range(10000))
print_arrays(arr, arr2)
