# Stack implementation in List without size limit

class Stack:
  def __init__(self) -> None:
      self.list = []

  def __str__(self) -> str:
      values = self.list.reverse()
      values = [str(x) for x in self.list]
      return '\n'.join(values)

  #isEmpty
  def isEmpty(self):
    if self.list == []:
      return True
    else:
      return False

  # push
  def push(self, value):
    self.list.append(value)
    return "The element has been successfully inserted"

  # pop
  def pop(self):
    if self.list == []:
      return "Stack is empty"
    else:
      return self.list.pop()

  # peek
  def peek(self):
    if self.list == []:
      return "Stack is empty"
    else:
      return self.list[-1]

  # delete list
  def delete(self):
    self.list = []


customStack = Stack()
customStack.push(0)
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())
print(customStack)