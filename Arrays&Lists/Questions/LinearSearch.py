import array as arr

ar = arr.array('i', [1,2,3,4,5,6,7,8,9,10])

def findNumber(arr, target):
  found = False
  for i in range(len(arr)):
    if target == arr[i]:
      found = True
      print("Found at: ", i)
      break
  if not found:
    print("Not Found!!!")


findNumber(ar, 18)