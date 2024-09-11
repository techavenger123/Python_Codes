# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:44:43 2024

@author: student
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal."

# Dog class inherits from Animal class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Cat class inherits from Animal class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # 
print(cat.speak())  # 