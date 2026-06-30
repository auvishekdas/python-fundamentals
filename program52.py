class People:
    Serial = ""
    Age = ""
    def __init__(self,Serial,Age):
        self.Serial = Serial
        self.Age = Age
    def display(self):
        print(f"Serial : {self.Serial}, Age : {self.Age}")
        
Hasan = People(11,35)        
Hasan.display()

Habib = People(12,25)
Habib.display()

