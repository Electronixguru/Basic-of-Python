from array import *

arr = array('i',[])

k = int(input("Enter the length of array: "))

for e in range(k):
    l=int(input("Enter the no: "))
    arr.append(l)
print(arr)

m=int(input("Enter no to find Position of: "))
n=1
for j in arr:
    if j ==m:
        print(n)
        break
    n+=1