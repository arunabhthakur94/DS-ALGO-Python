from random import randint

class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None
    self.prev = None

  def __str__(self):
      return str(self.value)

class LinkedList:
  def __str__(self, values = None):
    self.head = None
    self.tail = None

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next
  
  def __str__(self) -> str:
      values = [str(x.value) for x in self]
      return ' -> '.join(values)

  def __len__(self):
    count = 0
    node = self.head
    while node:
      count += 1
      node = node.next
    return count

  def add(self, value):
    newNode = Node(value)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode
    return self.tail

  def generate(self, n, min_value, max_value):
    self.head = None
    self.tail = None
    for i in range(n):
      self.add(randint(min_value, max_value))
    return self
      

# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(len(customLL))