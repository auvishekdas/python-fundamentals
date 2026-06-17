
#xargs
def student (*details):
    print(details)
student (1,"Nitai Das",5.00)     

#xargs
def student (*details):
    print(details[1])
student (1,"Nitai Das",5.00)

#xargs
def mix(*digits):
    sum = 0
    for num in digits:
         sum = sum + num
    print(sum)
mix(25,48,78)
mix(13,32,45)
mix(18,19)
   
    
