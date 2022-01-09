def bubbleSort(customList):
  for i in range(len(customList)-1):
    for j in range(len(customList)-i-1):
      if customList[j] > customList[j+1]:
        customList[j],customList[j+1] = customList[j+1],customList[j]
  print(customList)


customList = [9,1,3,6,8,4,7,5,2]
bubbleSort(customList)