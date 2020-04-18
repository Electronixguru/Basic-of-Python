def person(Name, **data):
    print(Name)
    for i,j in data.items():
        print(i,j)


person('Saurabh', age=21, No=9764607901, Gender='Male')