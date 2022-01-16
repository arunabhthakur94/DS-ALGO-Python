activity = [["A1", 0, 6],["A2", 3, 4],["A3", 1, 2],["A4", 5, 8],["A5", 5, 7],["A6", 8, 9]]

# Solution 1 using index parameter
def ActivitySelectionProblem1(activity):
  activity.sort(key=lambda x: x[2])
  index = 0
  firstActivity = activity[index][0]
  print(firstActivity)
  for i in range(len(activity)):
    if activity[i][1] > activity[index][2]:
      print(activity[i][0])
      index = i

# Solution 2 using last activity compeleted
def ActivitySelectionProblem2(activity):
  activity.sort(key = lambda x: x[2])
  currActivity = activity[0]
  print(currActivity[0])
  for i in range(1, len(activity)):
    if activity[i][1] > currActivity[2]:
      print(activity[i][0])
      currActivity = activity[i]

# TC: O(NlogN) SC: O(1)
ActivitySelectionProblem1(activity)
ActivitySelectionProblem2(activity)


