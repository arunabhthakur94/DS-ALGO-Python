def selectionSort(customList):
  for i in range(len(customList)):
    min_index = i
    for j in range(i+1, len(customList)):
      if customList[min_index] > customList[j]:
        min_index = j
    customList[i], customList[min_index] = customList[min_index], customList[i]
  print(customList)


customList = [9,1,3,6,8,4,7,5,2]
selectionSort(customList)
    