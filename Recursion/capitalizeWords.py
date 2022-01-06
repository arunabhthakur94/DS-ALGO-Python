def capitalizeWords(arr):
  resultArr = []
  if len(arr) == 0:
    return resultArr
  resultArr.append(arr[0].upper())
  return resultArr + capitalizeWords(arr[1:])


print(capitalizeWords(['car','bike','cycle']))