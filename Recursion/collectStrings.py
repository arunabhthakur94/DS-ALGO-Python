def collectStrings(obj):
  resultArr = []
  if len(obj) == 0:
    return resultArr
  
  for key in obj:
    if type(obj[key]) is str:
      resultArr.append(str(obj[key]))
    elif type(obj[key]) is dict:
      resultArr += collectStrings(obj[key])
  return resultArr



obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": "Two",
      "notANumber": "True",
      "alsoNotANumber": "yup"
    }
  }
}

print(collectStrings(obj1))