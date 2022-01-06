def findBinary(n):
  if n/2 == 0:
    return n
  else:
    return n%2 + 10 * findBinary(int(n/2))


print(findBinary(5))
print(findBinary(10))