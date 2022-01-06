def factorial(num):
  if num in [0,1]:
    return 1
  else:
    return num * factorial(num-1)

print(factorial(4))
print(factorial(10))
print(factorial(28))
print(factorial(35))