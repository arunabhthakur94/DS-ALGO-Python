class Stack:
  # TC: O(1) SC: O(1)
  def __init__(self, maxSize) -> None:
      self.list = []
      self.maxSize = maxSize
  
  # TC: O(n) SC: O(1)
  def __str__(self) -> str:
      values = self.list.reverse()
      values = [str(x) for x in self.list]
      return '\n'.join(values)

  # TC: O(1) SC: O(1)
  def isEmpty(self):
    if self.list == []:
      return True
    return False

  # TC: O(1) SC: O(1)
  def isFull(self):
    if len(self.list) == self.maxSize:
      return True
    else:
      return False
  
  # TC: O(1)/O(n^2) SC: O(1)
  def push(self, value):
    if self.isFull():
      return "Stack is Full"
    else:
      self.list.append(value)
      return "The element has been successfully inserted"

  # TC: O(1) SC: O(1)
  def pop(self):
    if self.isEmpty():
      return "Stack is Empty"
    else:
      return self.list.pop()

  # TC: O(1) SC: O(1)
  def peek(self):
    if self.isEmpty():
      return "Stack is Empty"
    else:
      return self.list[-1]
      
  # TC: O(1) SC: O(1)
  def delete(self):
    self.list = []
    self.maxSize = 0


  
  

  