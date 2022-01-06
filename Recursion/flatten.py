def flatten(arr):
  resultArr = []
  for i in arr:
    if type(i) is list:
      resultArr.extend(flatten(i))
    else:
      resultArr.append(i)
  return resultArr


print(flatten([1,2,3,[4,5]]))