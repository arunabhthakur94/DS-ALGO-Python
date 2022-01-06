def isPalindrome(string):
  if len(string) in [0,1]:
    return True
  else:
    start = 0
    end = len(string)-1
    while start < end:
      if string[start] == string[end]:
        return isPalindrome(string[1:-1])
      else:
        return False
    


print(isPalindrome('awesome'))
print(isPalindrome('foobar'))
print(isPalindrome('tacocat'))