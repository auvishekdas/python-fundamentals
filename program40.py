def cube(a):
    return a*a*a
num = [2,4,6,8,10]
result = list(map(cube,num))
print(result)



num = [1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda a: a%2==0,num))
print(result)