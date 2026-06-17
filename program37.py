#xxargs
def student(**information):
    print(information)
student(id=11,name="Eamu",cgpa=4.98)

#xxargs
def student(**information):
    print(information["name"])
student(id=11,name="Eamu",cgpa=4.98)


