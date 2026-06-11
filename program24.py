# 1 + 2 + 3 + 4 + 5 + ... + n
n = int(input("Enter the last number : "))
sum = 0
for s in range ( 1, 1 + n, 1):
    sum =  sum + s
print(sum)         

# 2 + 4 + 6 + 8 + 10 + ... + n
n = int(input("Enter the last number : "))
sum = 0
for s in range (2, 1 + n, 2):
    sum = sum + s
print(sum)    
        
# 1*1 + 2*2 + 3*3 + 4*4 + 5*5 + ... + n*n
n= int(input("Enter the last number : "))
sum = 0
for s in range (1, 1 + n, 1):
    sum = sum + s*s
print(sum)    

# 1 * 2 * 3 * 4 * 5
n = int(input("Enter the last number : "))
sum = 1
for s in range(1, 1 + n, 1):
    sum = sum * s
print(sum)