class Car:
    wheels = 5
    def __init__(self):
        self.model = "Celario"
        self.mileage = 20

car1 = Car()

Car.wheels = 6

print("Model: ",car1.model,"Mileage", car1.mileage, "No of wheels: ", Car.wheels)