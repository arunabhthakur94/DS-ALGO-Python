def reverse(st):
  # return st[::-1]
  if len(st) == 1:
    return st[0]
  else:
    return st[-1] + reverse(st[:-1])


print(reverse('python'))