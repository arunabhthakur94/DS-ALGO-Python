def sumOfDigits(n):
  if n < 0:
    n = n * -1
  assert n >= 0 and int(n) == n, "Negative or decimal numbers are invalid"
  if n < 10:
    return n
  else:
    return sumOfDigits(int(n/10))+ sumOfDigits(int(n%10))


print(sumOfDigits(1.23))
print(sumOfDigits(-123))
print(sumOfDigits(123))