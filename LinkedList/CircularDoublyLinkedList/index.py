class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None
    self.prev = None

  def __str__(self):
    return str(self.value)


class CircularDoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def __iter__(self):
    node = self.head
    while node:
      yield node
      none = node.next
      if node == self.tail.next:
        break
  
  def createCDLL(self, value):
    node = Node(value)
    self.head = node
    self.tail = node
    node.next = node
    node.prev = node
    return "CDLL is created successfully!!!"
  
  def insertCDLL(self, value, pos):
    if self.head is None:
      return "Empty CDLL"
    else:
      node = Node(value)
      if pos == 0:
        node.next = self.head
        node.prev = self.tail
        self.head.prev = node
        self.head = node
        self.tail.next = node
      elif pos == -1:
        node.next = self.head
        node.prev = self.tail
        self.head.prev = node
        self.tail.next = node
        self.tail = node
      else:
        prevNode = self.head
        index = 0
        while index < pos-1:
          prevNode = prevNode.next
          index += 1
        nextNode = prevNode.next
        node.prev = prevNode
        node.next = nextNode
        prevNode.next = node
        nextNode.prev = node
      return "Node has been successfully created!!"


circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(0))
# print(circularDLL.insertCDLL(0,0))
# print(circularDLL.insertCDLL(1,1))
# print(circularDLL.insertCDLL(2,2))
# print(circularDLL.insertCDLL(3,3))
print([node.value for node in circularDLL])