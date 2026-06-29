class People:
    Serial = ""
    Age = ""
    def set_information(self,Serial,Age):
        self.Serial = Serial
        self.Age = Age
    def display(self):
        print(f"Serial : {self.Serial}, Age : {self.Age}")
        
Hasan = People()        
Hasan.set_information(11,35)
Hasan.display()

Habib = People()
Habib.set_information(12,25)
Habib.display()
