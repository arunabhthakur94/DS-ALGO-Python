import math

def binarySearch(arr, value):
  start = 0
  end = len(arr)-1
  mid = math.floor((start+end)/2)

  while start <= end and not (arr[mid] == value):
    if value < arr[mid]:
      end = mid-1
    else:
      start = mid+1
    mid = math.floor((start+end)/2)

  if arr[mid] == value:
    return mid
  else:
    return -1

arr = [10,20,30,40,50,60,70,80,90]
print(binarySearch(arr, 500))