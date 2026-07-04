class Shape:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2
    def area(self):
        print("I am area method")
        
class Triangle(Shape):
    def area(self):
        area = 0.5 * self.value1 * self.value2
        print("Area of Triangle",area)

class Rectangle(Shape):
    def area(self):
        area = self.value1 * self.value2
        print("Area of Rectangle",area)
    
t1 = Triangle(30,40)
t1.area()

r1 = Rectangle(50,60)
r1.area()