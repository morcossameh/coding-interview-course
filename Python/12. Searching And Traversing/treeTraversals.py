class Node:
  def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

def preorder(node):
  if node:
      print(node.value, end=' ')
      preorder(node.left)
      preorder(node.right)

def inorder(node):
  if node:
      inorder(node.left)
      print(node.value, end=' ')
      inorder(node.right)

def postorder(node):
  if node:
      postorder(node.left)
      postorder(node.right)
      print(node.value, end=' ')
    
#       4
#      / \
#     2   5
#    / \   \
#   1   3   6

# Example tree
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(6)

print("PreOrder Traversal:")
preorder(root)
print("\nInOrder Traversal:")
inorder(root)
print("\nPostOrder Traversal:")
postorder(root)