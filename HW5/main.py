from abc import ABC, abstractmethod
from math import sqrt

class Point:
    x = 0.0
    y = 0.0

class Line:
    pnt_a = Point()   #
    pnt_b = Point()
    
    def setLine(self, x1, y1, x2, y2):  #Готовые координаты
        self.pnt_a.x = x1
        self.pnt_a.y = y1
        self.pnt_b.x = x2
        self.pnt_b.y = y2

    def length(self): #Расчет длинны
         return sqrt((self.pnt_b.x - self.pnt_a.x)**2 + (self.pnt_b.y - self.pnt_a.y)**2)

class Shape(ABC):
    
    @abstractmethod     
    def area(self):
        pass
    
    @abstractmethod     
    def perimeter(self):
        pass


class Square(Line, Shape): #Квадрат
    @property
    def area(self): #Расчет площади
        self._area = super().length()**2
        return self._area

    @property
    def perimeter(self): #Расчет периметра
        self._perimeter = super().length()*4
        return self._perimeter


class Rect(Shape): #Прямоугольник
    diag = Line()
    
    @property
    def perimeter(self): #Расчет периметра
        return abs(self.diag.pnt_a.x - self.diag.pnt_b.x)*2 + abs(self.diag.pnt_a.y - self.diag.pnt_b.y)*2
    
    @property    
    def area(self): #Расчет площади
        return abs(self.diag.pnt_a.x - self.diag.pnt_b.x) * abs(self.diag.pnt_a.y - self.diag.pnt_b.y)


class Cube(Square): #Куб
    def volume(self): #Расчет обьема
        return super().area  * super().length()

ln = Line()
ln.setLine(5, 4, 9, 1) #Параметры  
print(f"Line Length:  {ln.length()}")
print(f"-"*20)

#Квадрат
sq = Square() #Вызов функции
sq.setLine(5, 4, 9, 1) #Параметры  
print(f"Square Length: {sq.length()}") #Длинна
print(f"Square Perimetr: {sq.perimeter}") #Периметер
print(f"Square Area: {sq.area}") #Площадь
print(f"-"*20) #Вывод результата

#Прямоугольник
rt = Rect() #Вызов функции
rt.diag.setLine(1, 1, 4, 4) #Параметры             
print(f"Rect Perimetr: {rt.perimeter}") #Периметер
print(f"Rect Area: {rt.area}") #Площадь
print(f"-"*20) #Вывод результата

#Куб
cb = Cube() #Вызов функции
cb.setLine(5, 4, 9, 1) #Параметры                 
print(f"Cube Volume: {cb.volume()}") #Вывод результата
