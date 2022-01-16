# TC: O(NlogN) SC: O(1)
class Item:
  def __init__(self, weight, value) -> None:
      self.weight = weight
      self.value = value
      self.ratio = value/weight


def fractionaKanpsack(items, capacity):
  items.sort(key = lambda x: x.ratio, reverse=True)
  totalValue = 0
  usedCapacity = 0

  for i in items:
    if usedCapacity + i.weight <= capacity:
      totalValue += i.value
      usedCapacity += i.weight
    else:
      diff = capacity - usedCapacity
      value = i.ratio * diff
      usedCapacity += diff
      totalValue += value
    
    if usedCapacity == capacity:
      break
  print("Total value obtained:" + str(totalValue))

item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
cList = [item1, item2, item3]

fractionaKanpsack(cList, 50)