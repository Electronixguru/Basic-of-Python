def Generator():
    n=1
    while(n<=10):
        num = n*n
        n+=1
        yield num

value = Generator()

for i in value:
    print(i)