class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x*self.y

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)
    def area(self):
        return 3.14*super().area()
class Square(Shape):
    def __init__(self,side):
        self.side = side
        super().__init__(side,side)
    def area(self):
        return super().area()
rec = Shape(3,5)
print(rec.area())
c = Circle(10)
print(c.area())
sq = Square(4)
print(sq.area())