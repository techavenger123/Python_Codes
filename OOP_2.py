# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:42:00 2024

@author: student
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Method to calculate area
    def area(self):
        return self.width * self.height

    # Method to calculate perimeter
    def perimeter(self):
        return 2 * (self.width + self.height)

# Create an object
rect = Rectangle(10, 5)

# Accessing methods
print(f"Area: {rect.area()}")  # Output: Area: 50
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 30