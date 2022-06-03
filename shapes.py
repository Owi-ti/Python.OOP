from math import pi

#1. Class Circle
#   A Circle instance accepts attribute radius (r)
#   It has a method area that returns the area (A) of the circle using the formula A=πr2
#   It has a method to calculate circumference (c) using the formula C=2πr

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        pi=3.14
        return self.radius**2*pi
    
    def circumference(self):
        pi=3.14
        return 2*self.radius*pi

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.circumference())





# 2.Class Square
#   A Square instance accepts the attribute side (a)
#   It has method area that returns the area (A) of the square using the formula A=a2
#   It has a method to calculate the perimeter (P) of the square using the formula P=4a

class Square():
    def __init__(self, a):
        self.side = a

    def area(self):
        return self.side*2
    
    def perimetre(self):
        return 4*self.side

NewSquare = Square(8)
print(NewSquare.area())
print(NewSquare.perimetre())



# 3.Class Rectangle
#   A Rectangle instance accepts two sides of a rectangle (w,l)
#   It has method to calculate the area (A) of the rectangle using the formula A=wl
#   It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)


class Rectangle():
    def __init__(self,l,w):
        self.legnth = l
        self.width=w

    def area(self):
        return (self.legnth*self.width)
    
    def perimetre(self):
        return 2*(self.legnth + self.width)

NewRectangle = Rectangle(8,6)
print(NewRectangle.area())
print(NewRectangle.perimetre())




# 4.Class Sphere
#   A Sphere Instance accepts the radius of the sphere (r)
#   It has a method to calculate the surface area (A) using the formula A=4πr2
#   It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)

class Sphere():
    def __init__(self, r):
        self.radius = r

    def surface_area(self):
        pi=3.14
        return self.radius**2*4*pi
    
    def volume(self):
        pi=3.14
        return (self.radius**3*pi)*4/3

NewSphere = Sphere(8)
print(NewSphere.surface_area())
print(NewSphere.volume())
        