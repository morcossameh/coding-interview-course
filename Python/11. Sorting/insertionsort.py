def insertionSort(arr):
  n = len(arr)

  for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = key
    
    print(f"Step {i}: {arr}")

arr = [64, 34, 25, 12, 22, 11, 90]
insertionSort(arr)
print("Sorted array: ", arr)
