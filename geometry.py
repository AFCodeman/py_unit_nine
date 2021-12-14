import rectangle
import triangle

rect = rectangle.Rectangle(4, 5)
tang = rectangle.Rectangle(11,7)
le = rectangle.Rectangle(1,1000)
print("Rectangle Perimeter. Rectangle Area")
print (rect.perimeter(), rect.area())
print (tang.perimeter(), tang.area())
print(le.perimeter(), le.area())

tri = triangle.Triangle(1, 3, 5)
ang = triangle.Triangle(1400, 14, 140)
le = triangle.Triangle(1, 1, 50000)
print("Triangle Perimeter. Triangle Area")
print(tri.perimeter(), tri.area())
print(ang.perimeter(), ang.area())
print(le.perimeter(), le.area())