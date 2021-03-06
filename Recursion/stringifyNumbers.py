obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": "True",
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

def stringifyNumbers(obj):
  for key in obj:
    if type(obj[key]) is int:
      obj[key] = str(obj[key])
    elif type(obj[key]) is dict:
      obj[key] = stringifyNumbers(obj[key])
  return obj


print(stringifyNumbers(obj1))
print(stringifyNumbers(obj2))