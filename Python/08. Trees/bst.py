class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None

  def insert(self, data):
    new_node = Node(data)
    if self.root is None:
      self.root = new_node
      return

    current = self.root
    while current:
      if data < current.data:
        if current.left is None:
          current.left = new_node
          current = None
        else:
          current = current.left
      else:
        if current.right is None:
          current.right = new_node
          current = None
        else:
          current = current.right

  def search(self, data):
    current = self.root
    while current:
      if current.data == data:
        return True
      elif data < current.data:
        current = current.left
      else:
        current = current.right
    return False

  def display(self):
    if self.root is None:
      print("Tree is empty")
    else:
      self._inorder_traversal(self.root)
      print()

  def _inorder_traversal(self, node):
    stack = []
    current = node
    while stack or current:
      if current:
        stack.append(current)
        current = current.left
      else:
        current = stack.pop()
        print(current.data, end=" ")
        current = current.right

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
