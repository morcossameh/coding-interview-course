class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0

  def push(self, data):
    new_node = Node(data)
    new_node.next = self.top
    self.top = new_node
    self.size += 1

  def pop(self):
    if self.is_empty():
      raise IndexError("Pop from empty stack")

    popped_node = self.top
    self.top = self.top.next
    self.size -= 1
    return popped_node.data

  def peek(self):
    if self.is_empty():
      raise IndexError("Pop from empty stack")

    return self.top.data

  def is_empty(self):
    return self.size == 0

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())


# 4 popped_node
# 3 top
# 2
# 1
