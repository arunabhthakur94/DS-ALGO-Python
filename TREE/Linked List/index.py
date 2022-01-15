# Creation of a tree TC: O(1) SC:O(1)
# Traverse all NodeList
# Insertion of a node
# Deletion of a node
# Search for a Value
# Deletion of tree
import QueueLinkedList as queue


class TreeNode:
  def __init__(self, data) -> None:
    self.data = data
    self.leftChild = None
    self.rightChild = None

newBT = TreeNode('Drinks')
hot = TreeNode('Hot')
cold = TreeNode('Cold')
newBT.leftChild = hot
newBT.rightChild = cold

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
hot.leftChild = tea
hot.rightChild = coffee

cola = TreeNode("Cola")
fanta = TreeNode("fanta")
cold.leftChild = cola
cold.rightChild = fanta

# Pre-Order Traversal TC: O(N) SC:O(N)
def preOrderTraversal(rootNode):
  if not rootNode:
    return
  print(rootNode.data)
  preOrderTraversal(rootNode.leftChild)
  preOrderTraversal(rootNode.rightChild)

# In-Order Traversal TC: O(N) SC:O(N)
def inOrderTraversal(rootNode):
  if not rootNode:
    return
  inOrderTraversal(rootNode.leftChild)
  print(rootNode.data)
  inOrderTraversal(rootNode.rightChild)

# Post-Order Traversal TC: O(N) SC:O(N)
def postOrderTraversal(rootNode):
  if not rootNode:
    return
  postOrderTraversal(rootNode.leftChild)
  postOrderTraversal(rootNode.rightChild)
  print(rootNode.data)


# Level-Order Traversal TC: O(N) SC:O(N)
def levelOrderTraversal(rootNode):
  if not rootNode:
    return
  else:
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
      root = customQueue.dequeue()
      print(root.value.data)
      if root.value.leftChild is not None:
        customQueue.enqueue(root.value.leftChild)
      if root.value.rightChild is not None:
        customQueue.enqueue(root.value.rightChild)

# Search value TC: O(N) SC:O(N)
def searchNode(rootNode, target):
  if not rootNode or target is None:
    return "The BT/target value does not exist"
  else:
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
      root = customQueue.dequeue()
      if root.value.data == target:
        return "Success"
      if root.value.leftChild is not None:
        customQueue.enqueue(root.value.leftChild)
      if root.value.rightChild is not None:
        customQueue.enqueue(root.value.rightChild)
    return "TargetNode is not available"

# Search value TC: O(N) SC:O(N)
def insertNode(rootNode, data):
  newNode = TreeNode(data)
  if not rootNode:
    rootNode = newNode
  else:
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
      root = customQueue.dequeue()
      if root.value.leftChild is not None:
        customQueue.enqueue(root.value.leftChild)
      else:
        root.value.leftChild = newNode
        return "Added successfully"
      if root.value.rightChild is not None:
        customQueue.enqueue(root.value.rightChild)
      else:
        root.value.rightChild = newNode
        return "Added successfully"

def getDeepestNode(rootNode):
  if not rootNode:
    return "The BT value does not exist"
  else:
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
      root = customQueue.dequeue()
      if root.value.leftChild is not None:
        customQueue.enqueue(root.value.leftChild)
      if root.value.rightChild is not None:
        customQueue.enqueue(root.value.rightChild)
    deepest = root.value
    return deepest

def deleteDeepestNode(rootNode, dnode):
  if not rootNode:
    return "The BT value does not exist"
  else:
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
      root = customQueue.dequeue()
      if root.value is dnode:
        root.value = None
        return
      if root.value.rightChild:
        if root.value.rightChild is dnode:
          root.value.rightChild = None
          return
        else:
          customQueue.enqueue(root.value.rightChild)
      if root.value.leftChild:
        if root.value.leftChild is dnode:
          root.value.leftChild = None
          return
        else:
          customQueue.enqueue(root.value.leftChild)


def deleteNode(rootNode, node):
  if not rootNode:
    return "The BT value does not exist"
  else:
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
      root = customQueue.dequeue()
      if root.value.data == node:
        deepestnode = getDeepestNode(rootNode)
        root.value.data = deepestnode.data
        deleteDeepestNode(rootNode, deepestnode)
        return "The node has been successfully deleted"
      if root.value.leftChild is not None:
        customQueue.enqueue(root.value.leftChild)
      if root.value.rightChild is not None:
        customQueue.enqueue(root.value.rightChild)
    return "Failed to delete"

def deleteBT(rootNode):
  if not rootNode:
    return "The BT value does not exist"
  else:
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None

  

print("Pre-Order Traversal")
preOrderTraversal(newBT)
print("In-Order Traversal")
inOrderTraversal(newBT)
print("post-Order Traversal")
postOrderTraversal(newBT)
print("level-Order Traversal")
levelOrderTraversal(newBT)
print(searchNode(newBT, "Tea1"))
print(insertNode(newBT, "GreenTea"))
newNode = getDeepestNode(newBT)
levelOrderTraversal(newBT)
deleteDeepestNode(newBT, newNode)
levelOrderTraversal(newBT)
deleteBT(newBT)
levelOrderTraversal(newBT)





      

  