# TC: O(N) SC:O(1)
def coinChange(totalNumber, coinsList):
  N = totalNumber
  coinsList.sort(reverse=True)
  index = 0
  while N > 0:
    if N >= coinsList[index]:
      print(coinsList[index])
      N -= coinsList[index]
    else:
      index += 1

coins = [1,2,3,5,20,50,100,500]
coinChange(1994, coins)