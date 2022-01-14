from array import *

# creation
# syntax
# array(typecode, [])
# i for integer
arr1 = array('i', [1,2,3,5,6])
# d for double type
arr2 = array('d' , [1.1,2.2,3.3,4.4])

# insertion of value
# Time complexity :
# O(1) -> insertion at last place else it is O(n)
# Space complexity: O(1)
arr1.insert(0, 0)
arr1.insert(4,4)
arr1.insert(len(arr1), 7)
print(arr1)