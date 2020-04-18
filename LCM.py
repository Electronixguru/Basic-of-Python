num1= float(input("Enter a two positive integer to find LCM: "))
num2 = float(input("Enter a two positive integer to find LCM: "))


if(num1 > num2):
    greater = num1
else:
    greater = num2

while(True):
    if(greater%num1==0 and greater%num2==0):
        print("LCM is ", greater)
        break;
    greater+=1

