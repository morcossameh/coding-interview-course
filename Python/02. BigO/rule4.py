def print_single_pairs(arr): 
  n = len(arr) # O(1)
  
  for i in range(n): # O(n)
    print(arr[i])
  
  for i in range(n): # O(n^2)
    for j in range(n):
      print(arr[i], arr[j])


# Example usage
data = [1, 3, 2, 3, 4, 1, 5]
print_single_pairs(data)


# O(n^2 + n + 1) => O(n^2)
10000 + 100 + 1

# O(n^3 + n^2 + n + 1) => O(n^3)
1000000 + 10000 + 100 + 1
