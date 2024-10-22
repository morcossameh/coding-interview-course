class HashTable:
  def __init__(self, size=10):
      self.size = size
      self.table = [[] for _ in range(size)]

  def hash_function(self, key):
    return hash(key) % self.size

  def insert(self, key, value):
    index = self.hash_function(key)
    items = self.table[index]
    items.append([key, value])

  def get(self, key):
    index = self.hash_function(key)
    items = self.table[index]
    for item in items:
      if item[0] == key:
        return item[1]

  def remove(self, key):
    index = self.hash_function(key)
    items = self.table[index]
    for j, item in enumerate(items):
      if item[0] == key:
        items.pop(j)

  def print_hash(self):
    print(self.table)

my_hash_table = HashTable()

my_hash_table.insert(1, "Badr")
my_hash_table.insert(2, "Menna")
my_hash_table.insert(3, "Yehia")

my_hash_table.print_hash()

my_hash_table.insert(11, "Adel")

my_hash_table.print_hash()

print(my_hash_table.get(2))

my_hash_table.remove(3)

my_hash_table.print_hash()
