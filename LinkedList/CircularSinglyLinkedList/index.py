class Node:
  def __init__(self, value=0):
    self.value = value
    self.next = None

class CSLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def __iter__(self):
    node = self.head
    while node:
      yield node
      if node.next == self.head:
        break
      node = node.next
  
  def __str__(self):
    csll = [str(node.value) for node in self]
    return " ".join(csll)

  def createCSLL(self, value):
    newNode = Node(value)
    self.head = newNode
    self.tail = newNode
    newNode.next = newNode
    return "CSLL has been created"
  
  def insertCSLL(self, value, pos):
    newNode = Node(value)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
      newNode.next = newNode
    else:
      if pos == 0:
        newNode.next = self.head
        self.head = newNode
        self.tail.next = newNode
      elif pos == -1:
        newNode.next = self.tail.next
        self.tail.next = newNode
        self.tail = newNode
      else:
        tempNode = self.head
        index = 0
        while index < pos-1:
          tempNode = tempNode.next
          index += 1
        if(tempNode.next == self.head):
          newNode.next = tempNode.next
          tempNode.next = newNode
          self.tail = newNode
        else:  
          newNode.next = tempNode.next
          tempNode.next = newNode
    return "The Node has been created succesfully"

  def traverseCSLL(self):
    if self.head is None:
      print("Empty Circular Singly Linked List")
    else:
      node = self.head
      while node:
        print(node.value)
        node = node.next
        if node == self.head:
          break

  def searchNode(self, value):
    if self.head is None:
      print("Empty Circular Singly Linked List")
    else:
      node = self.head
      index = 0
      while node:
        if node.value == value:
          return index
        node = node.next
        index += 1
        if node == self.head:
          return "The node does not exist in the CSLL"

  def deleteNode(self, pos):
    if self.head is None:
      print("Empty Circular Singly Linked List")
    elif self.head == self.tail:
      self.head.next = None
      self.head = None
      self.tail = None
    else:
      if pos == 0:
        self.head = self.head.next
        self.tail.next = self.head
      elif pos == -1:
        node = self.head
        while node:
          if node.next == self.tail:
            break
          node = node.next
        node.next = self.head
        self.tail = node
      else:
        node = self.head
        index = 0
        while index < pos-1:
          node = node.next
          index += 1
          if node == self.head:
            return "Out of index"
        temp = node.next
        node.next = temp.next

  def deleteCSLL(self):
    self.head = None
    self.tail.next = None
    self.tail = None
    return "Deleted succesfully!"



circularSinglyLinkedList = CSLinkedList()
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)

# circularSinglyLinkedList.head = node1
# node1.next = node2
# node2.next = node3
# node3.next = node1
# circularSinglyLinkedList.tail = node3
circularSinglyLinkedList.createCSLL(0)
circularSinglyLinkedList.insertCSLL(1,1)
circularSinglyLinkedList.insertCSLL(2,2)
circularSinglyLinkedList.insertCSLL(3,3)
circularSinglyLinkedList.insertCSLL(4,4)
circularSinglyLinkedList.insertCSLL(44,5)


# circularSinglyLinkedList.traverseCSLL()
# print(circularSinglyLinkedList.searchNode(444))

print(circularSinglyLinkedList)

print([node.value for node in circularSinglyLinkedList])

# circularSinglyLinkedList.deleteNode(0)
# circularSinglyLinkedList.deleteCSLL()

# print([node.value for node in circularSinglyLinkedList])
