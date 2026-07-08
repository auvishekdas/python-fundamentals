class Laptop:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def __eq__(self, other):
            return self.name == other.name and self.color == other.color
    def __str__(self):
            return (f"Name = {self.name}, Color = {self.color}")
        
            
        
laptop1 = Laptop("Apple","Black")
laptop2 = Laptop("Samsung","White")
print(laptop1==laptop2)
print(str(laptop2))