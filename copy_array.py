from numpy import *

arr1 = array([2,5,7,1,0,3,4,6,9,8])
arr2 = array([9,2,34,6,7,0,1,1,4,8])
arr1 = arr2
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))