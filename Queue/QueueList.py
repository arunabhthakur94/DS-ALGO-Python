class Queue:
  def __init__(self) -> None:
      self.List = []

  def __str__(self) -> str:
      values = [str(x) for x in self.List]
      values.reverse()
      return '\n'.join(values)

  def isEmpty(self):
    if self.List == []:
      return True
    else:
      return False

  def enqueue(self, value):
    self.List.insert(0, value)
    return "Value is inserted"

  def dequeue(self):
    if self.isEmpty():
      return "Queue is Empty"
    else:
      value = self.List.pop()
      return value
  
  def peek(self):
    if self.List == []:
      return "Queue is Empty"
    else:
      return self.List[-1]

  def delete(self):
    self.List = []
    return "Deleted Successfully"

customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.isEmpty())
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
print(customQueue.delete())
print(customQueue)
