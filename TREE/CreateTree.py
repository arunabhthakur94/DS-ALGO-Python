# Basic tree implementation using List

class TreeNode:
  def __init__(self, data, children = []) -> None:
      self.data = data
      self.children = children

  def __str__(self, level = 0) -> str:
      ret = " " * level + str(self.data) + '\n'
      for child in self.children:
        ret += child.__str__(level+1)
      return ret
  
  def addChild(self, childNode):
    self.children.append(childNode)


rootNode = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
rootNode.addChild(cold)
rootNode.addChild(hot)

tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
hot.addChild(tea)
hot.addChild(coffee)

cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])
cold.addChild(cola)
cold.addChild(fanta)

print(rootNode)
