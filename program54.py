class Laptop:
    def camera(self):
        print("You can use camera")
    def powerpoint(self):
        print("You can use powerpoint")        
class Apple:
    def camera(self):
        print("You can use camera")
    def powerpoint(self):
        print("You can use powerpoint")
class Doyel(Laptop):
    pass
                
l = Laptop()
l.camera()
l.powerpoint()

a = Apple()
a.camera()
a.powerpoint()
print(issubclass(Doyel,Laptop))
