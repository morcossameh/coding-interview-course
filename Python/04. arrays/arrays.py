arr = [1, 2, 3, 4, 5]
#      0  1  2  3  4

print(arr[0]) # O(1)

arr.append(6) # amortized O(1)
print(arr)

arr.insert(0, 7) # O(n)
print(arr)

print(arr.index(5)) # O(n)

arr.pop(3) # O(n)
print(arr)

arr.remove(7) # O(n)
print(arr)