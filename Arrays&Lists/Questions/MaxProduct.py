arr = [67,1,34,2,45,3,56,4,67,9,4,75];

def maxProduct(arr):
  firstHighest = 0
  secondHighest = 0

  for i in arr:
    if i > firstHighest:
      secondHighest = firstHighest
      firstHighest = i
    elif i ==  firstHighest:
      secondHighest = i
  
  print(firstHighest*secondHighest)

maxProduct(arr)