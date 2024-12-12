#create a Rectangle from a square and display their areas.

class Square:
    def __init__(self, x):
        self.x = x

    def Area(self):
        print('Area of the square = ', self.x * self.x)

class Rectangle(Square):
    def __init__(self, x, y):
        super().__init__(x)              #superclass object
        self.y = y
    def Area(self):
        print('Area of Rectangle : ', self.x * self.y)

r = Rectangle(11, 25)
r.Area()
