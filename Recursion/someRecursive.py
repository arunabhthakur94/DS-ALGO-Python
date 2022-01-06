def isOdd(num):
  if num%2 == 1:
    return True

def someRecursive(arr, callback):
  if len(arr) == 0:
    return False
  else:
    if callback(arr[0]):
      return True
    return someRecursive(arr[1:], callback)

print(someRecursive([1,2,3,4], isOdd))
print(someRecursive([4,6,8,9], isOdd))
print(someRecursive([4,6,8], isOdd))

