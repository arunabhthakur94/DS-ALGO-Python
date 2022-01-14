activity = [["A1", 0, 6],["A2", 3, 4],["A3", 1, 2],["A4", 5, 8],["A5", 5, 7],["A6", 8, 9]]

def ActivitySelectionProblem(activity):
  activity.sort(key=lambda x: x[2])
  index = 0
  firstActivity = activity[index][0]
  print(firstActivity)

  for j in range(len(activity)):
    if activity[j][1] > activity[index][2]:
      print(activity[j][0])
      index = j



ActivitySelectionProblem(activity)


