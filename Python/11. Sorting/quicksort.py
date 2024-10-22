def partition(arr, low, high):

  pivot = arr[high]

  i = low - 1

  # Traverse arr[low..high] and move all smaller
  # elements on the left side.
  for j in range(low, high):
    if arr[j] < pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  print(arr)
  return i + 1

def quick_sort(arr, low, high):
  if low < high:
    pivot = partition(arr, low, high)

    quick_sort(arr, low, pivot - 1)
    quick_sort(arr, pivot + 1, high)


arr = [10, 7, 8, 9, 1, 5]

# print("Given array is")
# print(arr)

quick_sort(arr, 0, len(arr) - 1)

# print("\nSorted array is")
# print(arr)
