def find(arr, target):
    for index, element in enumerate(arr):
      if element == target:
          return index
    
    return -1

data = [3, 1, 4, 1, 5, 9, 2, 6]
print(find(data, 3))