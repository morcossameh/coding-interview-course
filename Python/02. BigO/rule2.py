def process_list(arr): # O(5n + 6) => O(n + 1) => O(n)
  if len(arr) == 0: # O(1)
    return

  sum_of_elements = 0 # O(1)
  max_element = float('-inf') # O(1)
  min_element = float('inf') # O(1)

  for element in arr: # O(5n) => O(n)
      sum_of_elements += element # O(n)
      if element > max_element: # O(n)
          max_element = element # O(n)
      if element < min_element: # O(n)
          min_element = element # O(n)

  average = sum_of_elements / len(arr) # O(1)
  print(f"Sum: {sum_of_elements}, Max: {max_element}, Min: {min_element}, Average: {average}") # O(1)


data = [3, 1, 4, 1, 5, 9, 2, 6]
process_list(data)
