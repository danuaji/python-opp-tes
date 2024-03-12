import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius**2

# Contoh penggunaan polimorfisme
rectangle = Rectangle(5, 4)
circle = Circle(3)

print("Luas persegi panjang:", rectangle.calculate_area())  # Output: 20
print("Luas lingkaran:", circle.calculate_area())          # Output: 28.274333882308138
