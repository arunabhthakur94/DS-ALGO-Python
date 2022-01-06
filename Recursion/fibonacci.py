def fibonacciNumber(n):
  assert n >= 0 and int(n) == n, "Number should be of positive types"
  if n in [0,1]:
    return n
  else:
    return fibonacciNumber(n-1) + fibonacciNumber(n-2)


# print(fibonacciNumber(-6))
# print(fibonacciNumber(0))
# print(fibonacciNumber(6))
# print(fibonacciNumber(20))
print(fibonacciNumber(4))
print(fibonacciNumber(10))
print(fibonacciNumber(28))
print(fibonacciNumber(35))