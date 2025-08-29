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
      
        
class Vehicle:
    def _init_(self, wheels):
        self.wheels = wheels
        
class Car(Vehicle):
    pass

car = Car(4)
print(car.wheels) 


class Dog:
    def speak(self):
        return "Woohh!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
#Polymorphism in action
for animal in [Dog(), Cat()]:
    print(animal.speak())