class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def result(self):
        area = 0.5 * self.base * self.height
        print("Area = ",area)
        
t1 = Triangle(20,25)
t1.result()

t2 = Triangle(35,45)
t2.result()