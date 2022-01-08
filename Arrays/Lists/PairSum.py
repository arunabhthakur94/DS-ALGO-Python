# Time Complexitity: n^2
def findPair(arr, target):
  length = len(arr)
  for i in range(length):
    for j in range(i, length):
      if i != j and arr[i] + arr[j] == target:
        print(i, j)

# Time Complexitity: n
def findPair(arr, target):
  obj = {}
  for i in range(len(arr)):
    diff = target - arr[i]
    if diff in obj:
      print(obj[diff], i)
    else:
      obj[arr[i]] = i
  # print(obj)






arr = [2,6,3,9,11]
target = 9

findPair(arr, target)
findPair([2,7,11,15], target)
findPair([3,2,4], 6)
findPair([3,3], 6)

# obj = {"k1": 1, "k2": 2}
# print(obj)
# print(obj["k1"])
# print(obj.get("k3", None))
