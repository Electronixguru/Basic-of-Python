
num = int(input("Enter a number: "))
factorial = 1
for i in range(num,0,-1):
       factorial = factorial*i
print("The factorial of",num,"is",factorial)