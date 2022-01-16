def linearSearch(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return "Value not found!!"

arr = [1,6,3,5,8,9,4]
print(linearSearch(arr, 95))