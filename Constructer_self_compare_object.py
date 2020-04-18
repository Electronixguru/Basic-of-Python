class saurabh:

    def __init__(self):
        self.name = "Utkarsha"
        self.age=21

    def sauru(self):
        print("Name & Age: ", self.name, self.age)

    def update(self):
        self.age= 21
        self.name= "Saurabh"

    def compare(self, com2):
       if self.age == com2.age:
           return True
       else:
           return  False

com1 = saurabh()
com2 = saurabh()
com2.update()


if com1.compare(com2):
    print("They are same :)")
else:
    print("They are Diffrent :(")

print(com1.name, com1.age)
print(com2.name, com2.age)