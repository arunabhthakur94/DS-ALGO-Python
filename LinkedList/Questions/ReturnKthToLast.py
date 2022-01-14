from LinkedLinkedClass import LinkedList

def nthToLast(ll, n):
  p1 = ll.head
  count = 0

  currnode = ll.head
  while currnode:
    if count == n:
      p1 = p1.next
    else:
      count += 1
    currnode = currnode.next
  return p1


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthToLast(customLL, 2))