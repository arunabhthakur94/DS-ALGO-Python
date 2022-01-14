def permutation(list1, list2):
  isFound = True

  if len(list1) != len(list2):
    print("Not a permutaion of list")
  else:
    for i in list1:
      if i not in list2:
        isFound = False
        break

    if isFound:
      print("Permutaion")
    else:
      print("Not a permutaion of list")


list1=[1,2,3,4,5]
list2=[5,4,3,2,7]

permutation(list1,list2)