def recursiveRange(num):
  if num == 0:
    return num
  else:
    return num + recursiveRange(num-1)

print(recursiveRange(10))