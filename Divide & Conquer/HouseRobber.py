def HouseRobber(houses, currentHouse):
  if currentHouse >= len(houses):
    return 0
  else:
    stealFirstHouse = houses[currentHouse] + HouseRobber(houses, currentHouse+2)
    skipFirstHouse = HouseRobber(houses, currentHouse+1)
    return max(stealFirstHouse, skipFirstHouse)

houses  = [6,7,1,30,8,2,4]
print(HouseRobber(houses, 0))