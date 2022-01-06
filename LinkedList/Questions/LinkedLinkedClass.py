from random import randint

class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None
    self.prev = None

  def __str__(self):
    return str(self.value)

class LinkedList:
  def __init__(self, values = None):
    self.head = None
    self.tail = None

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next

  def __str__(self):
    arr = [str(node.value) for node in self]
    return ' '.join(arr)

  def __len__(self):
    length = 0
    node = self.head
    while node:
      length += 1
      node = node.next
    return length

  def add(self, value):
    node = Node(value)
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node
    return self.tail

  def generate(self, n, min_value, max_value):
    self.head = None
    self.tail = None
    for i in range(n):
      self.add(randint(min_value, max_value))
    return self


# ll = LinkedList()
# print(ll.generate(10, 10, 99))
# print(len(ll))
# print(ll)