class Queue:
  def __init__(self, maxSize) -> None:
      self.List = [None] * maxSize
      self.start = -1
      self.top = -1
      self.maxSize = maxSize

  def __str__(self) -> str:
      values = [str(x) for x in self.List]
      return ' '.join(values)

  def isFull(self):
    if self.top + 1 == self.start:
      return True
    elif self.start == 0 and self.top + 1 == self.maxSize:
      return True
    else:
      return False

  def isEmpty(self):
    if self.top == -1:
      return True
    else:
      return False

  def enqueue(self, value):
    if self.isFull():
      return "Queue is Full"
    else:
      if self.top + 1 == self.maxSize:
        self.top = 0
      else:
        self.top += 1
        if self.start == -1:
          self.start = 0
      self.List[self.top] = value
      return "Element added successfully"

  def dequeue(self):
    if self.isEmpty():
      return "Queue is Empty"
    else:
      first = self.List[self.start]
      start = self.start
      if self.start == self.top:
        self.start = -1
        self.top = -1
      elif self.start + 1 == self.maxSize:
        self.start = 0
      else:
        self.start += 1
      self.List[start] = None
      return first

  def peek(self):
    if self.isEmpty():
      return "Queue is Empty"
    else:
      return self.List[self.start]

  def delete(self):
    if self.isEmpty():
      return "Queue is Empty"
    else:
      self.List = [None] * self.maxSize
      self.start = -1
      self.top = -1


customQueue = Queue(3)
print(customQueue.isFull())
print(customQueue.isEmpty())