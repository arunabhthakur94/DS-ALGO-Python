# GCD = Greatest Common Divisor
def findGCD(n, m):
  assert n > 0 and m > 0 and int(n) == n and int(m) == m, "Positive numbers are valid only"
  if n%m == 0:
    return m
  else:
    return findGCD(m, n%m)

print(findGCD(36,18))