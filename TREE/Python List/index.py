class BinaryTree:
  def __init__(self, maxSize) -> None:
      self.customList = [None] * maxSize
      self.lastUsedIndex = 0
      self.maxSize = maxSize

  def insertNode(self, value):
    if self.lastUsedIndex + 1 == self.maxSize:
      return "BT is full"
    else:
      self.lastUsedIndex += 1
      self.customList[self.lastUsedIndex] = value
      return "the value has been inserted successfully"
  
  def searchNode(self, value):
    for i in self.customList:
      if i == value:
        return "Found"
    return "Not found"

  def preOrderTraversal(self, index=1):
    if index > self.lastUsedIndex:
      return
    print(self.customList[index])
    self.preOrderTraversal(2*index)
    self.preOrderTraversal(2*index+1)

  def inOrderTraversal(self, index=1):
    if index > self.lastUsedIndex:
      return
    self.inOrderTraversal(2*index)
    print(self.customList[index])
    self.inOrderTraversal(2*index+1)
  
  def postOrderTraversal(self, index=1):
    if index > self.lastUsedIndex:
      return
    self.postOrderTraversal(2*index)
    self.postOrderTraversal(2*index+1)
    print(self.customList[index])

  def levelOrderTraversal(self):
    for i in self.customList:
      print(i)

  def deleteNode(self, value):
    if self.lastUsedIndex == 0:
      return "Empty BT"
    for i in range(1, self.lastUsedIndex+1):
      if self.customList[i] == value:
        self.customList[i] = self.customList[self.lastUsedIndex]
        self.customList[self.lastUsedIndex] = None
        self.lastUsedIndex -= 1
        return "The nide has been deleted successfully"

  def deleteBt(self):
    self.customList = [None] * self.maxSize
    self.lastUsedIndex = 0

newBt = BinaryTree(10)
print(newBt.insertNode("Drinks"))
print(newBt.insertNode("Hot"))
print(newBt.insertNode("Cold"))
print(newBt.insertNode("Tea"))
print(newBt.insertNode("Coffee"))
print(newBt.insertNode("Cola"))
print(newBt.insertNode("Fanta"))
print(newBt.customList)
newBt.preOrderTraversal()

