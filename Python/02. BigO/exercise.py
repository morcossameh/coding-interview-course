def compute_complex(arr1, arr2):
  for i in range(len(arr2)): # O(m)
    arr2[i] *= 2

  for i in range(len(arr1)): # O(n)
    arr1[i] *= 5
        
  for i in range(len(arr1)): # O(n^3)
    for j in range(len(arr1)):
      for k in range(len(arr1)):
        arr1[i] += arr1[j] * arr1[k]
  
  return arr1, arr2

# O(n^3 + n + m) => O(n^3 + m)
#                    8 < 1000