class Node:
  def __init__(self, value = None) -> None:
      self.value = value
      self.next = None

  def __str__(self) -> str:
      return str(self.value)

class LinkedList:
  def __init__(self) -> None:
      self.head = None
  
  def __iter__(self) -> None:
    node = self.head
    while node:
      yield node
      node = node.next

class Stack:
  def __init__(self) -> None:
      self.LinkedList = LinkedList()
  
  def __str__(self) -> str:
      values = [str(x.value) for x in self.LinkedList]
      return '\n'.join(values)

  def isEmpty(self):
    if self.LinkedList.head is None:
      return True
    else:
      return False

  def push(self, value):
    node = Node(value)
    node.next = self.LinkedList.head
    self.LinkedList.head = node
    return "Inserted Successfully"

  def pop(self):
    if self.LinkedList.head is None:
      return "Stack is Empty"
    else:
      nodeValue = self.LinkedList.head.value
      self.LinkedList.head = self.LinkedList.head.next
      return nodeValue

  def peek(self):
    if self.LinkedList.head is None:
      return "Stack is Empty"
    else:
      return self.LinkedList.head.value

  def delete(self):
    self.LinkedList.head = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print(customStack.pop())
print(customStack.isEmpty())

# TC: O(1) and SC: O(1)
# Each function has same TC and SC
  