from LinkedLinkedClass import LinkedList

def RemoveDups(linkedList):
  tempSet = []

  node  = linkedList.head
  tempSet.append(node.value)
  while node.next:
    if node.next.value not in tempSet:
      tempSet.append(node.next.value)
      node = node.next
    else:
      node.next = node.next.next
      node = node.next.next
  return linkedList


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(RemoveDups(customLL))


