def find_duplicate_pairs(arr):
  duplicates = []
  n = len(arr)

  for i in range(n):
      for j in range(n):
          if i != j and arr[i] == arr[j]:
              duplicates.append(arr[j])

  return duplicates

# Example usage
data = [1, 3, 2, 3, 4, 1, 5]
duplicate_pairs = find_duplicate_pairs(data)
