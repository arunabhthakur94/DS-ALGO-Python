class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

  def __str__(self):
    return str(self.value)

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next
    
  def createDLL(self, value):
    node = Node(value)
    self.head = node
    self.tail = node
    return "DLL is created successfully"

  # Insertion Method in Doubly Linked List
  def insertNode(self, value, pos):
    if self.head is Node:
      print("Empty Doubly Linked List")
    else:
      newNode = Node(value)
      if pos == 0:
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
      elif pos == -1:
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
      else:
        tempNode = self.head
        index = 0
        while index < pos-1:
          tempNode = tempNode.next
          index += 1
        if tempNode.next is None:
          tempNode.next = newNode
          newNode.prev = tempNode
        else:
          nextNode = tempNode.next
          newNode.next = nextNode
          newNode.prev = tempNode
          tempNode.next = newNode
          nextNode.prev = nextNode
  
  def traversalDLL(self):
    if self.head is None:
      print("Empty DLL")
    else:
      node = self.head
      while node:
        print(node.value)
        node = node.next

  def reverseDLL(self):
    if self.head is None:
      print("Empty DLL")
    else:
      node = self.tail
      while node:
        print(node.value)
        node = node.prev

  def searchNode(self, value):
    if self.head is None:
      print("Empty DLL")
    else:
      node = self.head
      while node:
        if node.value == value:
          return "Found"
        node = node.next
      return "NOT FOUND!!"

  def deleteNode(self, pos):
    if self.head is None:
      print("Empty DLL")
    else:
      if pos == 0:
        if self.head == self.tail:
          self.head = None
          self.tail = None
        else:
          self.head = self.head.next
          self.head.prev = None
      elif pos == -1:
        if self.head == self.tail:
          self.head = None
          self.tail = None
        else:
          self.tail = self.tail.prev
          self.tail.next = None
      else:
        node = self.head
        index = 0
        while index < pos-1:
          node = node.next
          index += 1
        nodeToBeDeleted = node.next
        nextNode = nodeToBeDeleted.next
        node.next = nextNode
        nextNode.prev = node
  
  def deleteDLL(self):
    if self.head is None:
      print("Empty DLL")
    else:
      tempNode = self.head
      while tempNode:
        tempNode.prev = None
        tempNode = tempNode.next
      self.head = None
      self.tail = None
    print("DLL has been successfully deleted")







doublyLL = DoublyLinkedList()
doublyLL.createDLL(0)
doublyLL.insertNode(1,1)
doublyLL.insertNode(2,2)
doublyLL.insertNode(3,3)
doublyLL.insertNode(4,4)

print([node.value for node in doublyLL])
# print(doublyLL.traversalDLL())
# print(doublyLL.reverseDLL())