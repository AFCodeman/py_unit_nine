import math
class Triangle:


    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return(self.side1 + self.side2 + self.side3)

    def area(self):
        s = self.perimeter/2
        area = sqrt(s(s - self.side1)(s - self.side2)(s - self.side3))
        return area
