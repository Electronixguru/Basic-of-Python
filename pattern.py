'''
for i in range (5,0,-1):
    for j in range(i):
        print("#",end="")

    print()
'''

for i in range(1,5):
    for j in range(5-i):
        print(i,end="")
        i+=1
    print()