# Given N, find the number of ways to express N as a sum of 1, 3 and 4
def NumberFactor(N):
  if N in [0,1,2]:
    return 1
  elif N == 3:
    return 2
  else:
    com1 = NumberFactor(N-1)
    com2 = NumberFactor(N-3)
    com3 = NumberFactor(N-4)
    return com1 + com2 + com3

print(NumberFactor(5))