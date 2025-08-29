#OOP
#Defining a class

class Car:
    color = "green"

    #Method
    def drive(self):
        print("The car moves")

#Creating an object
my_car = Car()
print(my_car.color)
my_car.drive()


class Car:
    def _init_(self, color, model):
        self.color = color #Instance variable
        self.model = model #Instance variable
        
#Creating objects with unique attributes
car1 = Car("blue",  "Tesla")
car2 = Car("yellow", "Honda")

#Output
print(car1.color) 
print(car2.model)
