# Creation of Node Class
class Node:
  def __init__(self, value=0):
    self.value = value
    self.next = None

# Creation of Singly Linked List Class
class SLinkedList:
  # __init__ method : constructor
  def __init__(self):
    self.head = None
    self.tail = None
  # __iter__ method : Used for iteration of SLL
  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next
  # insertion in SLL
  def insertValueSLL(self, value, pos):
    newNode = Node(value)
    # Empty SLL
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      # First pos
      if pos == 0:
        newNode.next = self.head.next
        self.head = newNode
      # Last pos
      elif pos == -1:
        self.tail.next = newNode
        self.tail = newNode
      # Random pos
      else:
        tempNode = self.head
        index = 0
        while index < pos-1:
          tempNode = tempNode.next
          index += 1
        newNode.next = tempNode.next
        tempNode.next = newNode
        if tempNode == self.tail:
          self.tail = newNode

  # Traversal of SLL
  def traverseSLL(self):
    # Empty SLL
    if self.head is None:
      print("The given SLL is empty")
    else:
      node = self.head
      while node:
        print(node.value)
        node = node.next

  # Search value and return index of it if present
  def searchValueSLL(self, value):
    # Empty SLL
    if self.head is None:
      print("The given SLL is empty")
    else:
      node = self.head
      index = 0
      while node:
        if node.value == value:
          return index
        node = node.next
        index += 1
      return "Value is not present in SLL"

  # Deletion of a first occurance of value from SLL
  def deleteValueSLL(self, value):
    # Empty SLL
    if self.head is None:
      print("The given SLL is empty")
    else:
      currentNode = self.head
      prevNode = None
      while currentNode:
        if currentNode.value == value:
          prevNode.next = currentNode.next
          currentNode.next = None
          break
        prevNode = currentNode
        currentNode = currentNode.next

  # Deletion of Node:
  def deleteNodeSLL(self, pos):
    # Empty SLL
    if self.head is None:
      print("The given SLL is empty")
    # has only one node
    elif self.head == self.tail and (pos == 0 or pos == -1):
      self.head = None
      self.tail = None
    else:
      # First
      if pos == 0:
        self.head = self.head.next
      # Last
      elif pos == -1:
        node = self.head
        while node:
          if node.next == self.tail:
            node.next = None
            self.tail = node
          node = node.next
      # Random pos
      else:
        node = self.head
        index = 0
        while index < pos-1:
          node = node.next
          index += 1
        nodeToBeDeleted = node.next
        node.next = nodeToBeDeleted.next
  # Delete SLL
  def deleteSLL(self):
    # Empty SLL
    if self.head is None:
      print("The given SLL is empty")
    else:
      self.head = None
      self.tail = None

        
          


singlyLinkedList = SLinkedList()
singlyLinkedList.insertValueSLL(0, 0)
singlyLinkedList.insertValueSLL(1, 1)
singlyLinkedList.insertValueSLL(3, 2)
singlyLinkedList.insertValueSLL(2, 2)

singlyLinkedList.traverseSLL()
singlyLinkedList.deleteValueSLL(2)
print(singlyLinkedList.searchValueSLL(3))
singlyLinkedList.deleteNodeSLL(2)
singlyLinkedList.deleteSLL()
print([node.value for node in singlyLinkedList])

