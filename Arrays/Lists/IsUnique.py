# arr = [67,1,34,2,45,3,56,4,67,9,4,75];
arr = [1,2,3,4,5,6,7,8,9]

def isUnique(arr):
  dummy = []
  for i in arr:
    if i not in dummy:
      dummy.append(i)
  print(dummy, arr)
  if len(dummy) == len(arr):
    print("UNIQUE LIST")
  else:
    print("NOT UNIQUE")

isUnique(arr)