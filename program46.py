try:
    my_list = [40,30,20,0]
    result = my_list[1] / my_list[3]
    print(result)
    print("Successful")
except ZeroDivisionError:
    print("ZeroDivisionError")
    print("Successful")
    
    
try:
    my_list = [40,30,20,0]
    result = my_list[1] / my_list[2]
    print(result)
    print("Successful")
except SyntaxError:
    print("SyntaxError")
    print("Successful")
    
  
   