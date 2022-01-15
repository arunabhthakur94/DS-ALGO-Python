class Node:
  def __init__(self, value = None) -> None:
      self.value = value
      self.next = None

  def __str__(self) -> str:
      return str(self.value)

class LinkedList:
  def __init__(self) -> None:
      self.head = None
      self.tail = None

  def __iter__(self) -> None:
      node = self.head
      while node:
        yield node
        node = node.next


class Queue:
  def __init__(self) -> None:
      self.List = LinkedList()

  def __str__(self) -> str:
      values = [str(x.value) for x in self.List]
      return ' '.join(values)

  def isEmpty(self):
    if self.List.head is None:
      return True
    else:
      return False

  def enqueue(self, value):
    node = Node(value)
    if self.List.head is None:
      self.List.head = node
      self.List.tail = node
    else:
      self.List.tail.next = node
      self.List.tail = node
  
  def dequeue(self):
    if self.isEmpty():
      return "Queue is Empty"
    else:
      if self.List.head == self.List.tail:
        self.List.head = None
        self.List.tail = None
      else:
        self.List.head = self.List.head.next

  def peek(self):
    if self.isEmpty():
      return "Queue is Empty"
    else:
      return self.List.head.value



customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
customQueue.dequeue()
print(customQueue)


  