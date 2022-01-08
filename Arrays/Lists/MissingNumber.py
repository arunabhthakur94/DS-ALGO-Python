def missingNumber(li, n):
  totSum = n*(n+1)/2
  listSum = sum(li)
  print(totSum-listSum)



missingNumber([1,2,3,4,5,6,7,9,10], 10)

