#Chapter # 53-61 Classes

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = "200 AMP"        #Default attribute

    def descriptionCar(self):
        print(f"The make of car is {self.make}")
        print(f"The model of car is {self.model}")
        print(f"The year of car is {self.year}")

    def move(self):
        print(f"The {self.make} can move with speed")

    def applyBreak(self):
        print(f"The {self.model} has applied the break")

    def setBatterySize(self, newSize):
        self.battery = newSize
    
    def getBatterySize(self):
        print(f"The size of your car's battery is {self.battery} ")

#Create Object For Car Class
car1 = Car("Honda", "Civic", 2020)
car2 = Car("BMW", "Hi2020", 2021)

#Access attributes with objects
print(car1.make)
print(car2.make)

#Access method with objects
print(car1.move())
print(car2.descriptionCar())

#Changing an attributes value (Direct hit attributes value)
car1.make = "Ford"
print("New car make is:", car1.make)

#Get default attributes
print("Default attributes value =",car1.battery)

#Update/Change default attributes value directly
car1.battery = "300 AMP"
print("After Changed 'battery' value by attribute =",car1.battery)

#Update/Change default attributes value by method
car1.setBatterySize("400 AMP")

#Get default attributes value by method
print(car1.getBatterySize())