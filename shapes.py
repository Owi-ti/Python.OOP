from cmath import pi

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





# 2.
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



# 3.
class Rectangle():
    def __init__(self,l,w):
        self.side1 = l
        self.side2 =w

    def area(self):
        return self.side1*self.side2
    
    def perimetre(self):
        return 2*(self.side1 + self.side2)

NewRectangle = Rectangle(8,6)
print(NewRectangle.area())
print(NewRectangle.perimetre())




# 4.
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
        