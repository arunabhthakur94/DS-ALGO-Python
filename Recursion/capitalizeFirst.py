def capitalizeFirst(arr):
  resultArr = []
  if len(arr) == 0:
    return resultArr
  resultArr.append(arr[0][0].upper() + arr[0][1:])
  return resultArr + capitalizeFirst(arr[1:])


print(capitalizeFirst(['car','bike','cycle']))