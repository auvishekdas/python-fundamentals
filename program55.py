class laptop:
    def __init__(self):
        print("I am in laptop class")
class apple(laptop):
    pass
a = apple()


class laptop:
    def __init__(self):
        print("I am in laptop class")
class apple(laptop):
    def __init__(self):
        print("I am in apple class")
a = apple()


class laptop:
    def __init__(self):
        print("I am in laptop class")
class apple(laptop):
   def __init__(self):
       super().__init__()
       print("I am in apple class") 
a = apple()        