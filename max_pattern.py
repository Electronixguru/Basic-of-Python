'''
*
**
***
num = int(input("Enter the no of rows: "))
for i in range (1,num+1):
    for j in range(i):
        print("*",end="")
    print()
'''
'''
num = int(input("Enter the no of rows: "))
for i in range (num):
    for j in range(num-i):
        print("*",end="")
    print()
'''
'''
num = int(input("Enter the no of rows: "))
for i in range (1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''
'''
   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   * 
num = int(input("Enter the no of rows: "))
for row in range (0,num):
    for col in range(0,num-row-1):
        print(end=" ")
    for col in range(0, row+1):
        print('*',end=" ")
    print()

for row in range (num,0,-1):
    for col in range(0,num-row+1):
        print(end=" ")
    for col in range(0,row-1):
        print('*',end=" ")
    print()
'''
'''
num= int(input("Enter no of row: "))
for row in range(1,num+1):
    for col in range(1,row+1):
        print("*",end=" ")
    print()

for row in range(num,0,-1):
    for col in range(row-1,0,-1):
        print("*",end=" ")
    print()
'''