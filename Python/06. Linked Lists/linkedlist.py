class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head = new_node

  def insert_at_index(self, data, index):
    if index == 0:
      self.insert_at_beginning(data)

    position = 0
    current_node = self.head
    while current_node != None and position + 1 != index:
      position += 1
      current_node = current_node.next

    if current_node != None:
      new_node = Node(data)
      new_node.next = current_node.next
      current_node.next = new_node
    else:
      print("Index out of range")

  def remove_first_node(self):
    if self.head == None:
      return

    self.head = self.head.next

  def remove_at_index(self, index):
    if self.head == None:
      return

    if index == 0:
      self.remove_first_node()

    position = 0
    current_node = self.head
    while current_node != None and position + 1 != index:
      position += 1
      current_node = current_node.next

    if current_node != None:
      current_node.next = current_node.next.next
    else:
      print("Index out of range")

  def display(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

ll = LinkedList()
ll.insert_at_beginning(0)
ll.insert_at_beginning(1)
ll.insert_at_beginning(2)
ll.insert_at_index(3, 1)
ll.remove_first_node()
ll.remove_at_index(1)
ll.remove_at_index(10)
ll.display()

# 5  ->  7  ->  9  -> 11  -> 13  ->  None
#              curr
