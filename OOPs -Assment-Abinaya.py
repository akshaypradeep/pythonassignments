#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 1: Basic Animal Class
Create a base class called Animal.
Define a name attribute.
Create a makeSound() method. This method should print "Generic animal sound".
Create a subclass called Dog that inherits from Animal.
Override the makeSound() method. This method should print "Woof!".
Create a subclass called Cat that inherits from Animal.
Override the makeSound() method. This method should print "Meow!".
Create instances of Animal, Dog, and Cat.
Call the makeSound() method on each instance. 
Assignment 2: Vehicle Class
1. Create a base class called Vehicle.
Define attributes like name and color.
Create a drive() method. This method should print "Generic vehicle is driving".
2. Create a subclass called Car that inherits from Vehicle.
Override the drive() method. This method should print "The car is driving".
3. Create a subclass called Truck that inherits from Vehicle.
Override the drive() method. This method should print "The truck is driving".
4. Create instances of Vehicle, Car, and Truck.
Call the drive() method on each instance. 
Assignment 3: Shape Class 
Create a base class called Shape. 
Define a getArea() method that returns 0. 
Create a subclass called Rectangle that inherits from Shape. 
Override the getArea() method to calculate the area of a rectangle (area = length * width). 
Add attributes like length and width. 
Create a subclass called Circle that inherits from Shape. 
Override the getArea() method to calculate the area of a circle (area = pi * radius^2). 
Add an attribute like radius. 
Create instances of Shape, Rectangle, and Circle. 
Call the getArea() method on each instance and print the results.


# In[1]:


'''
Assignment 1: Basic Animal Class
Create a base class called Animal.
Define a name attribute.
Create a makeSound() method. This method should print "Generic animal sound".
Create a subclass called Dog that inherits from Animal.
Override the makeSound() method. This method should print "Woof!".
Create a subclass called Cat that inherits from Animal.
Override the makeSound() method. This method should print "Meow!".
Create instances of Animal, Dog, and Cat.
Call the makeSound() method on each instance. '''



class Animal:
    def __init__(self,name):
        self.name=name
        
    def makeSound(self):
        print("Generic animal Sound")
        
class Dog(Animal):
    def makSound(self):
        print("Woof!")

class Cat(Animal):
    def makeSound(self):
        print("Meow!")
        
 # Create instances
animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call makeSound() on each instance
print(f"{animal.name} says:", end=" ")
animal.makeSound()

print(f"{dog.name} says:", end=" ")
dog.makeSound()

print(f"{cat.name} says:", end=" ")
cat.makeSound()       
    


# In[3]:


'''
Assignment 2: Vehicle Class
1. Create a base class called Vehicle.
Define attributes like name and color.
Create a drive() method. This method should print "Generic vehicle is driving".
2. Create a subclass called Car that inherits from Vehicle.
Override the drive() method. This method should print "The car is driving".
3. Create a subclass called Truck that inherits from Vehicle.
Override the drive() method. This method should print "The truck is driving".
4. Create instances of Vehicle, Car, and Truck.
Call the drive() method on each instance. '''

class Vehicle:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        
    def drive(self):
        print("Generic vehicle is driving")
        
class Car(Vehicle):
    def drive(self):
        print("The car is driving")

class Truck(Vehicle):
    def drive(self):
        print("The truck is driving")
        
 # Create instances
vehicle = Vehicle("General ", "White")
car = Car("BMW","Blue")
truck = Truck("Tata motors","Brown")

# Call makeSound() on each instance
print(f"{vehicle.name} says:", end=" ")
vehicle.drive()

print(f"{car.name} says:", end=" ")
car.drive()

print(f"{truck.name} says:", end=" ")
truck.drive()       



# In[ ]:


'''
Assignment 3: Shape Class 
Create a base class called Shape. 
Define a getArea() method that returns 0. 
Create a subclass called Rectangle that inherits from Shape. 
Override the getArea() method to calculate the area of a rectangle (area = length * width). 
Add attributes like length and width. 
Create a subclass called Circle that inherits from Shape. 
Override the getArea() method to calculate the area of a circle (area = pi * radius^2). 
Add an attribute like radius. 
Create instances of Shape, Rectangle, and Circle. 
Call the getArea() method on each instance and print the results.
'''



import math

# Parent class
class Shape:
    def getArea(self):
        return 0

# Rectangle childclass or subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

# Creating instances
shape = Shape()
rectangle = Rectangle(5, 3)
circle = Circle(4)

# Calling getArea() and printing results
print("Shape area:", shape.getArea())          # Expected: 0
print("Rectangle area:", rectangle.getArea())  # Expected: 15
print("Circle area:", circle.getArea())        # Expected: ~50.27

