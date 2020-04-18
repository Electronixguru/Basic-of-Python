from array import *

arr = array('i',[])

k = int(input("Enter the length of array: "))

for i in range (k):
    l = int(input("Enter the no: "))
    arr.append(l)
print(arr)
o=int(input("Enter no you want index of: "))
n=0
for j in arr:

    if j==o:
        print(n)
        break
    n+=1
