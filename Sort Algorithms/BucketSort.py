# Number of buckets = round(sqrt(length of array))
# Appropriate bucket for each element = ceil(value * Number of buckets / max_value)

import math

def insertionSort(customList):
  for i in range(1, len(customList)):
    key = customList[i]
    j = i-1
    while j>=0 and key < customList[j]:
      customList[j+1] = customList[j]
      j -= 1
    customList[j+1] = key
  return customList

def bucketSort(customList):
  numberOfBuckets = round(math.sqrt(len(customList)))
  maxValue = max(customList)
  arr = []

  for i in range(numberOfBuckets):
    arr.append([])

  for j in customList:
    bucket_index = math.ceil(j * numberOfBuckets / maxValue)
    arr[bucket_index-1].append(j)
  
  for index in range(len(arr)):
    arr[index] = insertionSort(arr[index])

  result = []
  for i in arr:
    result.extend(i)
  
  print(result)

  



customList = [9,1,3,6,8,4,7,5,2]
bucketSort(customList)