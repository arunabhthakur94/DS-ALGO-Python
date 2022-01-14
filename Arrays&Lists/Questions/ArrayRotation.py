arr = [[1,2,3],[4,5,6],[7,8,9]]
# print(len(arr)//2)

def rotate(arr):
  rows = len(arr)

  for rowLayer in range(rows//2):
    first = rowLayer
    last = rows-rowLayer-1
    for colLayer in range(first, last):
      # top element
      temp = arr[rowLayer][colLayer]
      # move left bottom to left top
      arr[rowLayer][colLayer] = arr[-colLayer-1][rowLayer]
      # move bottom right to bottom left
      arr[-colLayer-1][rowLayer] = arr[-rowLayer-1][-colLayer-1]
      # move top right to bottom right
      arr[-rowLayer-1][-colLayer-1] = arr[colLayer][-rowLayer-1]
      # move top to right
      arr[colLayer][-rowLayer-1] = temp

  print(arr)


rotate(arr)
