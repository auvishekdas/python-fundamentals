class X:
    def result1(self):
        print("I am inside X class")
class Y(X):
    def result2(self):
        print("I am inside Y class")
class Z(Y):
    def result3(self):
        print("I am inside Z class")        
value1 = Z()
value1.result1()
value1.result2()
value1.result3()

class T:
    def result1(self):
        print("I am inside T class")
class U(T):
    def result2(self):
        print("I am inside U class")
class V(U):
    def result3(self):
        super().result1()
        super().result2()
        print("I am inside V class")
        
value1 = V()
value1.result3()

