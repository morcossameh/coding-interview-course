class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def enqueue(self, data):
    new_node = Node(data)
    if self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.size += 1

  def dequeue(self):
    if self.is_empty():
      raise IndexError("Dequeue from empty queue")

    dequeued_node = self.head
    self.head = dequeued_node.next
    if self.head is None:
      self.tail = None
    self.size -= 1
    return dequeued_node.data

  def peek(self):
    if self.is_empty():
      raise IndexError("Peek from empty queue")

    return self.head.data

  def is_empty(self):
    return self.size == 0

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())

# dequeue
# 4 head 
# 3
# 2
# 1 tail
# enqueue
