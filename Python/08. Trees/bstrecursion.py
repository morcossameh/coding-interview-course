class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None

  def _insert_recursive(self, node, data):
    if data < node.data:
      # base case
      if node.left is None:
        node.left = Node(data)
      # recursive case
      else:
        self._insert_recursive(node.left, data)
    else:
      # base case
      if node.right is None:
        node.right = Node(data)
      # recursive case
      else:
        self._insert_recursive(node.right, data)
  
  def insert(self, data):
    if self.root is None:
      self.root = Node(data)
    else:
      self._insert_recursive(self.root, data)

  def _search_recursive(self, node, data):
    # base case
    if node is None:
      return False
    if node.data == data:
      return True

    # recursive case
    if data < node.data:
      return self._search_recursive(node.left, data)
    else:
      return self._search_recursive(node.right, data)

  def search(self, data):
    return self._search_recursive(self.root, data)

  def display(self):
    if self.root is None:
      print("Tree is empty")
    else:
      self._inorder_traversal(self.root)
      print()

  def _inorder_traversal(self, node):
    if node:
      self._inorder_traversal(node.left)
      print(node.data, end=' ')
      self._inorder_traversal(node.right)

bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(5)
bst.insert(1)
bst.insert(3)
bst.insert(6)
bst.display()

print(bst.search(1))
print(bst.search(10))

#       4
#      / \
#     2   5
#    / \   \
#   1   3   6
