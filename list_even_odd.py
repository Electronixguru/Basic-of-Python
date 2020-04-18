from array import *
def counter(lst):
    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst = array('i', [])
for k in lst:
    x = int(input("Enter the Length of list: "))
    for i in x:
        m=int(input("Enter the no's: "))
        m.append(lst)

even,odd=counter(lst)
print ("Even: ",even)
print("Odd: ",odd)
