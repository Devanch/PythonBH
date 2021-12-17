from abc import ABC, abstractmethod
from math import sqrt

class Point:
    x = 0.0
    y = 0.0

class Line:
    point_a = Point() 
    point_b = Point() 
    def len(self):
        return  sqrt((self.point_b.x - self.point_a.x)**2 + (self.point_b.y - self.point_a.y)**2)


class Shape(ABC): 
    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter

class Square(Line, Shape):
    def fun(self):
        return super().len() * 4
        self.perimeter = 10

    area = 20

class React(Shape):
    line = Line()

class Cube(Square):
    volume = 0;

ln = Line()
ln.point_a.x = 5
ln.point_a.y = 4
ln.point_b.x = 9
ln.point_b.y = 1
print(f"Line Length:  {ln.len()}")

sq = Square()
sq.point_a.x = 5
sq.point_a.y = 4
sq.point_b.x = 9
sq.point_b.y = 1
print(f"Square Length: {sq.len()}")
print(f"Square Perimetr: {sq.perimeter}")
print(f"Square Area: {sq.area}")
print(f"Square fun: {sq.fun()}")